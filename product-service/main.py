from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Products Service", 
    description="Microservice de gestion des produits",
    version="1.0"
)

@app.get("/")
def read_root():
    return {"message": "Products Service", "status": "running"}

products_db = [
    {"id": 1, "name": "Laptop", "price": 999.99},
    {"id": 2, "name": "Mouse", "price": 29.99},
    {"id": 3, "name": "Keyboard", "price": 79.99}
]

class Product(BaseModel):
    name: str
    price: float

@app.get("/products")
def get_all_products():
    return {"status": "success", "data": products_db}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products_db:
        if product["id"] == product_id:
            return {"status": "success", "data": product}
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products")
def create_product(product: Product):
    new_id = len(products_db) + 1
    new_product = {"id": new_id, "name": product.name, "price": product.price}
    products_db.append(new_product)
    return {"status": "success", "message": "Product created", "product_id": new_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
