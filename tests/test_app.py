# tests/test_main.py

from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_index_html():
    response = client.get("/")
    assert response.status_code == 200