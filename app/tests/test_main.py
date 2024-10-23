from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_allocate_vehicle():
    response = client.post("/allocate", json={"employee_id": 1, "vehicle_id": 1, "date": "2024-10-23"})
    assert response.status_code == 200
    assert response.json()["employee_id"] == 1

def test_get_allocations():
    response = client.get("/allocations", params={"employee_id": 1})
    assert response.status_code == 200
    assert len(response.json()) >= 1
