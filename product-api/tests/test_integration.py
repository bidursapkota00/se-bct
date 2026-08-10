import os
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app

# Use a separate test database
TEST_DATABASE_URL = os.environ.get(
    "TEST_DATABASE_URL",
    "postgresql://user:pass@localhost:5432/testdb",
)
test_engine = create_engine(TEST_DATABASE_URL)
TestSession = sessionmaker(bind=test_engine)


def override_get_db():
    db = TestSession()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db
client = TestClient(app)


@pytest.fixture(autouse=True)
def setup_database():
    """Create tables before each test and drop them after."""
    Base.metadata.create_all(bind=test_engine)
    yield
    Base.metadata.drop_all(bind=test_engine)


class TestCreateProduct:
    """Integration tests for POST /products."""

    def test_create_product(self):
        """Creating a product should return 201 with product data."""
        response = client.post("/products", json={"name": "Laptop", "price": 999.99})
        assert response.status_code == 201
        data = response.json()
        assert data["name"] == "Laptop"
        assert data["price"] == 999.99
        assert "id" in data

    def test_create_product_invalid_price(self):
        """Negative price should return 422 validation error."""
        response = client.post("/products", json={"name": "Mouse", "price": -10.0})
        assert response.status_code == 422

    def test_create_product_empty_name(self):
        """Empty name should return 422 validation error."""
        response = client.post("/products", json={"name": "", "price": 100.0})
        assert response.status_code == 422

    def test_create_product_missing_fields(self):
        """Missing fields should return 422 validation error."""
        response = client.post("/products", json={})
        assert response.status_code == 422


class TestReadProducts:
    """Integration tests for GET /products."""

    def test_list_empty(self):
        """Listing products when none exist should return an empty list."""
        response = client.get("/products")
        assert response.status_code == 200
        assert response.json() == []

    def test_list_after_create(self):
        """Listing products after creating one should return it."""
        client.post("/products", json={"name": "Keyboard", "price": 75.0})
        response = client.get("/products")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["name"] == "Keyboard"

    def test_get_product_by_id(self):
        """Getting a product by ID should return the correct product."""
        create_response = client.post("/products", json={"name": "Monitor", "price": 300.0})
        product_id = create_response.json()["id"]
        response = client.get(f"/products/{product_id}")
        assert response.status_code == 200
        assert response.json()["name"] == "Monitor"

    def test_get_product_not_found(self):
        """Getting a non-existent product should return 404."""
        response = client.get("/products/999")
        assert response.status_code == 404
        assert response.json()["detail"] == "Product not found"