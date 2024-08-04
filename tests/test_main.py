import pytest
from fastapi.testclient import TestClient
from app.main import app

# Create a TestClient instance to interact with the FastAPI app
client = TestClient(app)

def test_read_root():
    # Send a GET request to the root endpoint
    response = client.get("/")
    
    # Assert that the response status code is 200
    assert response.status_code == 200
    
    # Assert that the response contains the expected content
    assert b"<!DOCTYPE html>" in response.content
    assert b"<html>" in response.content
    assert b"</html>" in response.content