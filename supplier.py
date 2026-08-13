from sqlmodel import SQLModel, Field
from typing import Optional

class Supplier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    contact_person: str
    email: str
    phone: str
    is_active: bool = True

class SupplierCreate(SQLModel):
    name: str
    contact_person: str
    email: str
    phone: str