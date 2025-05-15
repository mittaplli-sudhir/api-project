import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.fixture
def create_sample_task():
    def _create_task(title="Sample", description="Sample description"):
        response = client.post("/tasks/", json={"title": title, "description": description})
        return response.json()
    return _create_task

# Positive Tests

def test_create_task(create_sample_task):
    task = create_sample_task("Test Create", "Create desc")
    assert task["title"] == "Test Create"

def test_read_task(create_sample_task):
    task = create_sample_task("Test Read", "Read desc")
    response = client.get(f"/tasks/{task['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Read"

def test_update_task(create_sample_task):
    task = create_sample_task("Old", "Old desc")
    response = client.put(f"/tasks/{task['id']}", json={"title": "Updated", "description": "Updated desc"})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated"

def test_delete_task(create_sample_task):
    task = create_sample_task("Delete", "Delete desc")
    response = client.delete(f"/tasks/{task['id']}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted"

# Negative Tests

def test_read_nonexistent_task():
    response = client.get("/tasks/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_update_nonexistent_task():
    response = client.put("/tasks/99999", json={"title": "X", "description": "Y"})
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_delete_nonexistent_task():
    response = client.delete("/tasks/99999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_create_invalid_task():
    response = client.post("/tasks/", json={"title": 123, "description": None})
    assert response.status_code == 422