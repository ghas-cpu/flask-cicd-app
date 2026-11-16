from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200  # التأكد أن الصفحة تفتح بنجاح

def test_addition():
    client = app.test_client()
    response = client.post("/", data={"n1": "15", "n2": "25"})
    assert "40.0".encode() in response.data  # التأكد أن 15 + 25 = 40.0
