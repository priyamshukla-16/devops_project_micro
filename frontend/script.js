const form = document.getElementById("orderForm");
const result = document.getElementById("result");
const submitButton = form.querySelector("button[type='submit']");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  if (!form.reportValidity()) return;

  const order = {
    name: document.getElementById("name").value.trim(),
    phone: document.getElementById("phone").value.trim(),
    product: document.getElementById("product").value,
    quantity: Number(document.getElementById("quantity").value),
    payment_method: document.getElementById("payment_method").value
  };

  result.className = "result show";
  result.textContent = "Placing your order…";
  submitButton.disabled = true;

  try {
    const response = await fetch("/api/orders", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(order)
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Order could not be placed.");

    result.className = "result show";
    result.innerHTML = `<h3>Order placed successfully ✓</h3><p><strong>Order ID:</strong> ${data.order_id}</p><p><strong>Product:</strong> ${escapeHtml(data.product)} × ${data.quantity}</p><p><strong>Total:</strong> ₹${Number(data.amount).toLocaleString("en-IN")}</p><p><strong>Payment:</strong> ${escapeHtml(data.payment_method)} · ${escapeHtml(data.payment?.payment_status || "Processed")}</p>`;
    form.reset();
  } catch (error) {
    result.className = "result show error";
    result.textContent = error.message || "Could not connect to the order service. Please try again.";
  } finally {
    submitButton.disabled = false;
  }
});

function escapeHtml(value) {
  return String(value).replace(/[&<>"']/g, (char) => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[char]));
}
