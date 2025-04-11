// product.js

// Obtener lista de productos
async function fetchProducts() {
    try {
        const response = await fetch('/products/');
        const products = await response.json();
        const productTable = document.getElementById('product-table');

        // Limpiar tabla
        productTable.innerHTML = '';
        products.forEach(product => {
            const row = `
                <tr>
                    <td>${product.barcode}</td>
                    <td>${product.name}</td>
                    <td>${product.cost_price}</td>
                    <td>${product.sale_price}</td>
                    <td>${product.stock}</td>
                    <td>
                        <button onclick="editProduct(${product.id})">Editar</button>
                        <button onclick="deleteProduct(${product.id})">Eliminar</button>
                    </td>
                </tr>
            `;
            productTable.innerHTML += row;
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// Agregar un nuevo producto
async function addProduct(product) {
    try {
        const response = await fetch('/products/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(product)
        });

        if (response.ok) {
            alert('Producto agregado exitosamente');
            fetchProducts(); // Refrescar la lista de productos
        } else {
            const data = await response.json();
            alert(data.message || 'Error al agregar producto');
        }
    } catch (error) {
        console.error('Error:', error);
    }
}