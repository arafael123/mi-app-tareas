from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200


def test_create_task():
    client = app.test_client()
    response = client.post("/tasks", json={"title": "Test"})
    assert response.status_code == 201


def test_get_tasks():
    client = app.test_client()
    response = client.get("/tasks")
    assert response.status_code == 200


def test_delete_task():
    client = app.test_client()
    client.post("/tasks", json={"title": "Eliminar"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200