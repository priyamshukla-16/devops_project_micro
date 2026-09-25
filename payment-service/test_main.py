from main import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["service"] == "Payment Service"
    assert data["status"] == "running"


def test_payment():
    client = app.test_client()

    response = client.post(
        "/payment",
        json={
            "order_id": 101,
            "amount": 55000
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["order_id"] == 101
    assert data["amount"] == 55000
    assert data["payment_status"] == "Payment Successful"