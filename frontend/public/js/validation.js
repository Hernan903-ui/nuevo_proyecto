// validation.js

// Validar el formulario de inicio de sesión
function validateLoginForm() {
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const errors = [];

    if (!email) {
        errors.push("El correo electrónico es obligatorio.");
    } else if (!/\S+@\S+\.\S+/.test(email)) {
        errors.push("El correo electrónico no tiene un formato válido.");
    }

    if (!password) {
        errors.push("La contraseña es obligatoria.");
    } else if (password.length < 6) {
        errors.push("La contraseña debe tener al menos 6 caracteres.");
    }

    return errors;
}

// Mostrar errores en el formulario
function showValidationErrors(errors) {
    const alertContainer = document.createElement("div");
    alertContainer.className = "alert alert-error";
    alertContainer.innerHTML = errors.join("<br>");
    const form = document.querySelector("form");
    form.prepend(alertContainer);

    setTimeout(() => alertContainer.remove(), 5000); // Remover después de 5 segundos
}

// Manejar la validación al enviar el formulario
document.getElementById("login-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const errors = validateLoginForm();

    if (errors.length > 0) {
        showValidationErrors(errors);
        return;
    }

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();

    // Llamar al método de login con AJAX
    login(email, password);
});