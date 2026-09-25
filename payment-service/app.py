from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "service": "Payment Service",
        "status": "running"
    })


@app.route("/payment", methods=["POST"])
def payment():

    data = request.get_json()

    order_id = data.get("order_id")
    amount = data.get("amount")

    return jsonify({
        "order_id": order_id,
        "amount": amount,
        "payment_status": "Payment Successful",
        "message": "Payment processed successfully"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)