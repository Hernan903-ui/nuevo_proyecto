document.getElementById('reset-password-form').addEventListener('submit', async (e) => {
    e.preventDefault();

    const token = document.getElementById('token').value;
    const newPassword = document.getElementById('new-password').value;

    try {
        const response = await fetch('/auth/reset-password', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ token, new_password: newPassword })
        });

        const data = await response.json();
        if (response.ok) {
            alert(data.message);
            window.location.href = '/login.html';
        } else {
            alert(data.error || 'Error al restablecer la contraseña');
        }
    } catch (error) {
        console.error('Error:', error);
    }
});