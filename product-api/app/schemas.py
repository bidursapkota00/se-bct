from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(min_length=1, max_length=100, examples=["Laptop"])
    price: float = Field(gt=0, examples=[999.99])


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

    model_config = {"from_attributes": True}