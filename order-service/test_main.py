from main import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["service"] == "Order Service"
    assert data["status"] == "running"


def test_orders():
    client = app.test_client()

    response = client.get("/orders")

    assert response.status_code == 200

    data = response.get_json()

    assert data["order_id"] == 101
    assert data["product"] == "Laptop"
    assert data["amount"] == 55000
    assert data["payment"]["payment_status"] == "Payment Successful"
