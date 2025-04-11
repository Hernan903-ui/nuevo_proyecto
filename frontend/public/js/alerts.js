// alerts.js

function showAlert(type, message) {
    const alertContainer = document.createElement("div");
    alertContainer.className = `alert ${type === "success" ? "alert-success" : "alert-error"}`;
    alertContainer.innerText = message;

    document.body.prepend(alertContainer);

    // Remover la alerta después de 5 segundos
    setTimeout(() => alertContainer.remove(), 5000);
}