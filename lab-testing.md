# Dockerized FastAPI Testing Workflows

![Bidur Sapkota](https://www.bidursapkota.com.np/images/gravatar.webp "Bidur Sapkota - Developer")&nbsp;[Bidur Sapkota](https://www.bidursapkota.com.np/)

![Dockerized FastAPI Testing Workflows by Bidur Sapkota](images/dockerized-fastapi-testing-1200.webp "Dockerized FastAPI Testing Workflows – Blog by Bidur Sapkota")

## Table of Contents

1. [Introduction](#introduction)
2. [Project Setup](#project-setup)
3. [Database Configuration](#database-configuration)
4. [Application Code](#application-code)
5. [Running with Docker Compose](#running-with-docker-compose)
6. [Swagger API Documentation](#swagger-api-documentation)
7. [Unit Testing](#unit-testing)
8. [Integration Testing](#integration-testing)
9. [Test Coverage Reports](#test-coverage-reports)
10. [Running Tests with Docker](#running-tests-with-docker)

---

## Introduction

Testing is the process of executing a program with the intent of finding errors. This lab builds a minimal FastAPI application that creates and reads products, backed by PostgreSQL. You will write unit tests to verify individual functions in isolation and integration tests to verify the full API with a real database. Finally, you will generate a coverage report to measure how much of your code is tested.

The application is intentionally minimal: a single `Product` resource with only `name` and `price`, supporting only Create and Read operations. This keeps the focus on testing methodology rather than application complexity.

### Testing Levels Covered

| Level               | What it tests                                 | Database        |
| ------------------- | --------------------------------------------- | --------------- |
| Unit Testing        | Individual functions and validation logic     | Not required    |
| Integration Testing | Full API request-response cycle with database | Real PostgreSQL |

---

## Project Setup

### Project Structure

```
product-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   └── database.py
├── tests/
│   ├── __init__.py
│   ├── test_unit.py
│   └── test_integration.py
├── Dockerfile
├── compose.yaml
├── requirements.txt
└── .dockerignore
```

### Create Project Directory

```bash
mkdir product-api
cd product-api
mkdir app tests
touch app/__init__.py tests/__init__.py
```

`mkdir -p` creates nested directories. `touch` creates empty `__init__.py` files that mark directories as Python packages.

### Create `requirements.txt`

```text
fastapi[standard]
sqlalchemy
psycopg2-binary
pytest
httpx
pytest-cov
```

`fastapi[standard]` includes FastAPI, Uvicorn, and Pydantic. `sqlalchemy` is the ORM for database operations. `psycopg2-binary` is the PostgreSQL driver for Python. `pytest` is the testing framework. `httpx` provides an async-capable HTTP client that FastAPI's test client uses. `pytest-cov` generates test coverage reports.

### Install Dependencies (Local Development)

```bash
python -m venv venv
source venv/bin/activate              # macOS/Linux
venv\Scripts\activate                 # Windows
pip install -r requirements.txt
```

---

## Database Configuration

### Create `app/database.py`

```python
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pass@localhost:5432/mydb")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

`os.getenv` reads the database URL from an environment variable, falling back to a default for local development. `create_engine` creates a connection pool to the database. `sessionmaker` creates a factory for database sessions. `DeclarativeBase` is the modern SQLAlchemy 2.0 base class for ORM models. `get_db` is a dependency that provides a database session to each request and ensures it is closed afterward.

---

## Application Code

### Create `app/schemas.py`

Pydantic schemas handle data validation. They define what data the API accepts and returns.

```python
from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100, examples=["Laptop"])
    price: float = Field(gt=0, examples=[999.99])


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

    model_config = {"from_attributes": True}
```

`BaseModel` is the Pydantic base class for data validation. `Field(min_length=1)` ensures the name is not empty. `Field(gt=0)` ensures the price is greater than zero. `examples` provides sample values for Swagger documentation. `model_config = {"from_attributes": True}` allows Pydantic to read data directly from SQLAlchemy model attributes.

### Create `app/models.py`

SQLAlchemy models define the database table structure.

```python
from sqlalchemy import Column, Integer, String, Float
from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    price = Column(Float, nullable=False)
```

`__tablename__` sets the database table name. `primary_key=True` makes `id` the primary key with auto-increment. `index=True` creates a database index on `id` for faster lookups. `nullable=False` prevents null values.

### Create `app/main.py`

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import engine, get_db, Base
from app.models import Product
from app.schemas import ProductCreate, ProductResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Product API",
    description="A simple API to create and read products",
    version="1.0.0",
)


@app.post("/products", response_model=ProductResponse, status_code=201)
def create_product(product: ProductCreate, db: Session = Depends(get_db)):
    db_product = Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@app.get("/products", response_model=list[ProductResponse])
def list_products(db: Session = Depends(get_db)):
    return db.query(Product).all()


@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
```

`Base.metadata.create_all(bind=engine)` creates all tables defined by ORM models if they do not already exist. `response_model=ProductResponse` tells FastAPI to serialize the response using the Pydantic schema. `status_code=201` returns HTTP 201 Created for successful product creation. `Depends(get_db)` injects a database session into the endpoint using FastAPI's dependency injection. `db.add()` stages the new object, `db.commit()` writes it to the database, and `db.refresh()` reloads it with the generated `id`. `HTTPException(status_code=404)` returns a 404 error if the product is not found.

---

## Running with Docker Compose

Docker Compose runs both PostgreSQL and the FastAPI app with a single command. The test database is also configured as part of the setup.

### Create `Dockerfile`

```dockerfile
FROM python:3.14-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
```

### Create `.dockerignore`

```text
venv/
.venv/
__pycache__/
*.pyc
.git/
.env
htmlcov/
.pytest_cache/
```

### Create `compose.yaml`

```yaml
services:
  api:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:pass@db:5432/mydb
    volumes:
      - ./app:/app/app
    depends_on:
      - db

  db:
    image: postgres:16
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=pass
      - POSTGRES_DB=mydb
    ports:
      - "5432:5432"
    volumes:
      - db-data:/var/lib/postgresql/data

volumes:
  db-data:
```

`depends_on` ensures the database container starts before the API container. The `db` service uses the official `postgres:16` image. Environment variables configure the database credentials. The API connects to PostgreSQL using `db` as the hostname because Compose creates a shared network. The `volumes` entry `./app:/app/app` mounts the local `app/` directory into the container so that code changes on the host are immediately reflected inside the container, enabling live reload.

### Start the Application

```bash
docker compose up --build
```

`--build` rebuilds the image if any files changed. The command runs in the foreground so you can see live logs from both the API and database containers. The API is available at `http://localhost:8000`. Swagger docs are at `http://localhost:8000/docs`. Because the Dockerfile uses `fastapi dev`, the server automatically reloads when you edit any file in the `app/` directory. Press `Ctrl+C` to stop all containers.

### Stop Everything

```bash
docker compose down -v
```

`-v` also removes the database volume, giving you a clean state for the next run.

---

## Swagger API Documentation

FastAPI automatically generates interactive API documentation from your code. No additional configuration is needed.

### Accessing Documentation

| URL                           | Description                              |
| ----------------------------- | ---------------------------------------- |
| `http://localhost:8000/docs`  | Swagger UI — interactive API explorer    |
| `http://localhost:8000/redoc` | ReDoc — alternative documentation viewer |

### What Swagger Shows

Swagger UI displays all endpoints with their HTTP methods, request/response schemas, validation rules, and example values. You can test endpoints directly from the browser by clicking "Try it out", filling in the fields, and clicking "Execute".

The documentation is generated from:

- **Route decorators**: `@app.post("/products")` defines the endpoint method and path.
- **Pydantic schemas**: `ProductCreate` and `ProductResponse` define request and response shapes.
- **Field validators**: `Field(min_length=1, gt=0)` documents validation constraints.
- **FastAPI metadata**: `title`, `description`, and `version` in `FastAPI()` appear in the docs header.

### Testing via Swagger

1. Open `http://localhost:8000/docs` in your browser.
2. Click on `POST /products` to expand it.
3. Click **Try it out**.
4. Enter a JSON body:

```json
{
  "name": "Laptop",
  "price": 999.99
}
```

5. Click **Execute**. You should see a `201` response with the created product including its `id`.
6. Click on `GET /products` and execute it to see the product you just created.

---

## Unit Testing

Unit tests verify individual components in isolation without requiring a database or network. Here we test Pydantic validation logic to confirm that valid data is accepted and invalid data is rejected.

### Create `tests/test_unit.py`

```python
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
```

`pytest.raises(Exception)` asserts that the code inside the block raises an exception. Each test method targets one specific validation rule. The class groups related tests together for readability.

### Run Unit Tests

```bash
pytest tests/test_unit.py -v
```

`-v` (verbose) shows each test name and its pass/fail status.

### Expected Output

```
tests/test_unit.py::TestProductValidation::test_valid_product PASSED
tests/test_unit.py::TestProductValidation::test_empty_name_rejected PASSED
tests/test_unit.py::TestProductValidation::test_zero_price_rejected PASSED
tests/test_unit.py::TestProductValidation::test_negative_price_rejected PASSED
tests/test_unit.py::TestProductValidation::test_missing_name_rejected PASSED
tests/test_unit.py::TestProductValidation::test_missing_price_rejected PASSED
tests/test_unit.py::TestProductValidation::test_name_max_length PASSED
tests/test_unit.py::TestProductValidation::test_name_at_max_length PASSED

============================== 8 passed ==============================
```

---

## Integration Testing

Integration tests verify that all components work together: the API endpoints, database operations, and data validation. These tests send real HTTP requests to the FastAPI app using a test database.

### Create `tests/test_integration.py`

```python
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base, get_db
from app.main import app

# Use a separate test database
TEST_DATABASE_URL = "postgresql://user:pass@localhost:5432/testdb"
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
```

`TestClient` from FastAPI wraps the app and sends HTTP requests without starting a real server. `create_engine(TEST_DATABASE_URL)` connects to a separate test database so tests do not affect production data. `app.dependency_overrides[get_db]` replaces the real database dependency with the test database. `@pytest.fixture(autouse=True)` runs `setup_database` automatically before and after every test. `Base.metadata.create_all()` creates tables before each test and `drop_all()` removes them after, ensuring each test starts with a clean database. `client.post("/products", json={...})` sends a POST request with JSON data. `response.status_code` and `response.json()` verify the HTTP status and response body.

### Run Integration Tests (Requires PostgreSQL)

The integration tests use a separate database called `testdb`. Create it inside the running PostgreSQL container:

```bash
docker compose exec db psql -U user -d mydb -c "CREATE DATABASE testdb;"
```

`exec db` runs a command inside the `db` container. `psql -U user` connects as the `user` role. `-c` executes the SQL command directly.

Start PostgreSQL first, then run:

```bash
pytest tests/test_integration.py -v
```

### Expected Output

```
tests/test_integration.py::TestCreateProduct::test_create_product PASSED
tests/test_integration.py::TestCreateProduct::test_create_product_invalid_price PASSED
tests/test_integration.py::TestCreateProduct::test_create_product_empty_name PASSED
tests/test_integration.py::TestCreateProduct::test_create_product_missing_fields PASSED
tests/test_integration.py::TestReadProducts::test_list_empty PASSED
tests/test_integration.py::TestReadProducts::test_list_after_create PASSED
tests/test_integration.py::TestReadProducts::test_get_product_by_id PASSED
tests/test_integration.py::TestReadProducts::test_get_product_not_found PASSED

============================== 8 passed ==============================
```

---

## Test Coverage Reports

Test coverage measures the percentage of your source code that is executed during testing. Higher coverage means more code paths are tested.

### Run Tests with Coverage

```bash
pytest --cov=app --cov-report=term-missing tests/
```

`--cov=app` measures coverage for the `app` package. `--cov-report=term-missing` shows coverage in the terminal and lists the specific line numbers that were not executed.

### Expected Output

```
tests/test_unit.py ........                                      [ 50%]
tests/test_integration.py ........                               [100%]

---------- coverage: ---- ----------
Name                 Stmts   Miss  Cover   Missing
----------------------------------------------------
app/__init__.py          0      0   100%
app/database.py          9      0   100%
app/main.py             18      0   100%
app/models.py            7      0   100%
app/schemas.py           8      0   100%
----------------------------------------------------
TOTAL                   42      0   100%

============================== 16 passed ==============================
```

`Stmts` is the total number of executable statements. `Miss` is the number of statements not executed during tests. `Cover` is the coverage percentage. `Missing` lists the line numbers that were not covered. 100% coverage means every line of application code was exercised by the tests.

### Generate HTML Coverage Report

```bash
pytest --cov=app --cov-report=html tests/
```

This creates an `htmlcov/` directory. Open `htmlcov/index.html` in a browser to see a detailed, interactive coverage report with color-coded source files showing covered and uncovered lines.
