from fastapi import FastAPI

from database import create_db
from products import router as product_router
from suppliers import router as supplier_router

app = FastAPI(
    title="TechVault Product API",
    version="1.0.0"
)

create_db()

app.include_router(product_router)
app.include_router(supplier_router)

@app.get("/")
def home():
    return {"message": "Welcome to TechVault Product API"}
