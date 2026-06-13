from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_dataset_summary_returns_counts():
    response = client.get("/datasets/summary")

    assert response.status_code == 200
    assert "real_images" in response.json()
    assert "ai_images" in response.json()