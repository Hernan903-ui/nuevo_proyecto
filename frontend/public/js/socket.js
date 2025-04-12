import { io } from "socket.io-client";

const socket = io("http://localhost:5000");

// Escuchar eventos de actualización de stock
socket.on("stock_updated", (data) => {
    console.log("Stock actualizado:", data);
    showNotification(`El stock de "${data.name}" se actualizó a ${data.quantity}`);
});

// Función para mostrar notificaciones
function showNotification(message) {
    const notification = document.createElement("div");
    notification.className = "notification";
    notification.textContent = message;

    document.body.appendChild(notification);

    setTimeout(() => {
        notification.remove();
    }, 5000);
}