from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Users Service",
    description="Microservice d'authentification et gestion utilisateurs",
    version="1.0"
)

# ROUTE RACINE AJOUTÉE
@app.get("/")
def read_root():
    return {"message": "Users Service", "status": "running"}

users_db = [
    {"id": 1, "username": "admin", "password": "admin123"},
    {"id": 2, "username": "user1", "password": "pass123"}
]

class User(BaseModel):
    username: str
    password: str

class LoginRequest(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(login_data: LoginRequest):
    for user in users_db:
        if user["username"] == login_data.username and user["password"] == login_data.password:
            return {"status": "success", "message": "Connexion réussie", "user_id": user["id"]}
    raise HTTPException(status_code=401, detail="Identifiants incorrects")

@app.post("/register")
def register(user: User):
    new_id = len(users_db) + 1
    new_user = {"id": new_id, "username": user.username, "password": user.password}
    users_db.append(new_user)
    return {"status": "success", "message": "Utilisateur créé", "user_id": new_id}

@app.get("/users")
def get_all_users():
    return {"status": "success", "data": users_db}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
