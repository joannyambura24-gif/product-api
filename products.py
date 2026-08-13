from fastapi import APIRouter

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.get("/")
def get_products():
    return {"message": "List of products"}

@router.post("/")
def create_product():
    return {"message": "Product created"}

@router.get("/{product_id}")
def get_product(product_id: int):
    return {"product_id": product_id}

@router.put("/{product_id}")
def update_product(product_id: int):
    return {"message": f"Product {product_id} updated"}

@router.delete("/{product_id}")
def delete_product(product_id: int):
    return {"message": f"Product {product_id} deleted"}