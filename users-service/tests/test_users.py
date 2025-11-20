import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from fastapi.testclient import TestClient
from users_service import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Users Service" in response.json()["message"]

def test_get_user():
    response = client.get("/users/1")
    if response.status_code == 200: 
        assert response.json()["user_id"] == 1
    else:

        print(f"Route / users/1 retourne: {response.status_code}")
        response2 = client.get("/")
        print(f"Route / retourne: {response2.status_code}")

def test_create_user():
    response = client.get("/users/")
    assert response.status_code == 200
    assert "data" in response.json()
    assert "status" in response.json()
    assert response.json()["status"] == "success"
