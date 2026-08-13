from fastapi import APIRouter

router = APIRouter(
    prefix="/suppliers",
    tags=["Suppliers"]
)

@router.get("/")
def get_suppliers():
    return {"message": "List of suppliers"}

@router.post("/")
def create_supplier():
    return {"message": "Supplier created"}