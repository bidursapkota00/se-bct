import pytest
from app.schemas import ProductCreate


class TestProductValidation:
    """Unit tests for Pydantic data validation."""

    def test_valid_product(self):
        """Valid data should create a ProductCreate instance."""
        product = ProductCreate(name="Laptop", price=999.99)
        assert product.name == "Laptop"
        assert product.price == 999.99

    def test_empty_name_rejected(self):
        """Empty name should raise a validation error."""
        with pytest.raises(Exception):
            ProductCreate(name="", price=100.0)

    def test_zero_price_rejected(self):
        """Zero price should raise a validation error."""
        with pytest.raises(Exception):
            ProductCreate(name="Mouse", price=0)

    def test_negative_price_rejected(self):
        """Negative price should raise a validation error."""
        with pytest.raises(Exception):
            ProductCreate(name="Mouse", price=-10.0)

    def test_missing_name_rejected(self):
        """Missing name field should raise a validation error."""
        with pytest.raises(Exception):
            ProductCreate(price=100.0)

    def test_missing_price_rejected(self):
        """Missing price field should raise a validation error."""
        with pytest.raises(Exception):
            ProductCreate(name="Mouse")

    def test_name_max_length(self):
        """Name exceeding 100 characters should raise a validation error."""
        with pytest.raises(Exception):
            ProductCreate(name="A" * 101, price=100.0)

    def test_name_at_max_length(self):
        """Name at exactly 100 characters should be accepted."""
        product = ProductCreate(name="A" * 100, price=100.0)
        assert len(product.name) == 100