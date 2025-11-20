from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(
    title="Orders Service",
    description="Microservice de gestion des commandes", 
    version="1.0"
)

@app.get("/")
def read_root():
    return {"message": "Orders Service", "status": "running"}

orders_db = [
    {"id": 1, "user_id": 1, "products": [1, 2], "total": 1029.98},
    {"id": 2, "user_id": 2, "products": [3], "total": 79.99}
]

class OrderItem(BaseModel):
    product_id: int
    quantity: int

class Order(BaseModel):
    user_id: int
    items: List[OrderItem]

@app.get("/orders")
def get_all_orders():
    return {"status": "success", "data": orders_db}

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders_db:
        if order["id"] == order_id:
            return {"status": "success", "data": order}
    raise HTTPException(status_code=404, detail="Order not found")

@app.post("/orders")
def create_order(order: Order):
    new_id = len(orders_db) + 1
    
    # Calcul du total (simplifié)
    total = 0.0
    for item in order.items:
        total += item.quantity * 99.99  # Prix fictif
    
    new_order = {
        "id": new_id, 
        "user_id": order.user_id, 
        "products": [item.product_id for item in order.items],
        "total": total
    }
    orders_db.append(new_order)
    return {"status": "success", "message": "Order created", "order_id": new_id}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
