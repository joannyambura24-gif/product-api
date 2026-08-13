from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: str
    brand: str
    category: str
    price: float
    stock: int
    warranty_months: int
    sku: str
    supplier_id: Optional[int] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

class ProductCreate(SQLModel):
    name: str
    description: str
    brand: str
    category: str
    price: float
    stock: int
    warranty_months: int
    sku: str
    supplier_id: Optional[int] = None