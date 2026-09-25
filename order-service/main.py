from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running"
    })


@app.route("/orders")
def orders():

    order_id = 101
    amount = 55000

    payment_data = {
        "order_id": order_id,
        "amount": amount
    }

    try:
        payment_response = requests.post(
            "http://payment-service:5002/payment",
            json=payment_data
        )

        payment_result = payment_response.json()

        return jsonify({
            "order_id": order_id,
            "product": "Laptop",
            "quantity": 1,
            "amount": amount,
            "payment": payment_result
        })

    except Exception as e:
        return jsonify({
            "error": "Payment Service unavailable",
            "details": str(e)
        }), 500


PRODUCT_PRICES = {
    "Samsung S24": 79999,
    "iPhone 15": 69999,
    "Google Pixel 8": 59999,
    "OnePlus 12": 64999,
}


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json(silent=True) or {}
    name = str(data.get("name", "")).strip()
    phone = str(data.get("phone", "")).strip()
    product = str(data.get("product", "")).strip()
    payment_method = str(data.get("payment_method", "Card")).strip()
    try:
        quantity = int(data.get("quantity", 1))
    except (TypeError, ValueError):
        quantity = 0

    if not name or not phone or product not in PRODUCT_PRICES or quantity < 1 or quantity > 99:
        return jsonify({"error": "Please enter valid order details."}), 400

    order_id = 1000 + __import__("random").randint(0, 8999)
    amount = PRODUCT_PRICES[product] * quantity
    payment_data = {"order_id": order_id, "amount": amount, "payment_method": payment_method}

    try:
        payment_response = requests.post(
            "http://payment-service:5002/payment",
            json=payment_data,
            timeout=10
        )
        payment_response.raise_for_status()
        payment_result = payment_response.json()
        return jsonify({
            "message": "Order placed successfully",
            "order_id": order_id,
            "name": name,
            "product": product,
            "quantity": quantity,
            "amount": amount,
            "payment_method": payment_method,
            "payment": payment_result
        }), 201
    except Exception as e:
        return jsonify({"error": "Payment Service unavailable", "details": str(e)}), 502


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)