// auth.js

// Función para iniciar sesión
async function login(email, password) {
    try {
        const response = await fetch('/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password })
        });

        const data = await response.json();
        if (response.ok) {
            alert('Inicio de sesión exitoso');
            localStorage.setItem('token', data.token); // Guardar token
            window.location.href = '/dashboard';
        } else {
            alert(data.message || 'Error al iniciar sesión');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}

// Función para cerrar sesión
function logout() {
    localStorage.removeItem('token');
    window.location.href = '/login';
}

function getRoleFromToken() {
    const token = localStorage.getItem('token');
    if (!token) return null;

    try {
        const payload = JSON.parse(atob(token.split('.')[1]));
        return payload.role;
    } catch (e) {
        console.error('Error al decodificar el token:', e);
        return null;
    }
}