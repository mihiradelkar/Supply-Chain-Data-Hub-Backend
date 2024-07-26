import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_companies():
    response = client.get("/api/companies/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_read_company():
    response = client.get("/api/companies/1")
    assert response.status_code == 200
    assert "company_id" in response.json()

def test_read_company_not_found():
    response = client.get("/api/companies/100")
    assert response.status_code == 404
