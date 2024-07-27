import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_locations():
    response = client.get("/api/locations/1")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_locations_not_found():
    response = client.get("/api/locations/100")
    assert response.status_code == 404
