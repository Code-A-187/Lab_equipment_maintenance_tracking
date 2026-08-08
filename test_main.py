from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response=client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Lab Operations API is online"}

def test_create_equipment():
    item = {"name": "Centrifuge", "status": "active", "maintenance_cost": 250}
    response = client.post(
        "/equipment/create", 
        json = item
        )
    data = response.json()
    assert response.status_code == 200
    assert response.json() == {
        "message": "Equipment successfully saved to database!",
        "data_received": item
    }

def test_get_equipment_cost():
    response = client.get(
        "/equipment/cost/?status=active"
    )
    data = response.json()
    assert data["status_filter"] == "active"
    assert "total_maintenance_cost" in data
    assert isinstance(data["total_maintenance_cost"], int)

def test_create_equipment_negative_cost():
    invalid_item = {"name": "Centrifuge", "status": "active", "maintenance_cost": -50}
    response = client.post(
            "/equipment/create", 
            json = invalid_item
            )
    assert response.status_code == 422

def test_create_equipment_short_name():
    invalid_item = {"name": "   A   ", "status": "active", "maintenance_cost": 250}
    response = client.post(
        "equipment/create",
        json = invalid_item
    )
    assert response.status_code == 422

def test_create_equipment_invalid_status():
    invalid_item = {"name": "Centrifuge", "status": "broken_xyz", "maintenance_cost": 250}
    response = client.post(
        "equipment/create",
        json=invalid_item
    )
    assert response.status_code == 422