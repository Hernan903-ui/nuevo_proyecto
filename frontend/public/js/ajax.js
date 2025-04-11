// ajax.js

async function fetchProducts() {
    try {
        const response = await fetch("/api/products");
        if (!response.ok) {
            throw new Error("Error al obtener los productos.");
        }

        const products = await response.json();
        const tableBody = document.getElementById("product-table");
        tableBody.innerHTML = ""; // Limpiar la tabla antes de llenarla

        products.forEach((product) => {
            const row = document.createElement("tr");
            row.innerHTML = `
                <td>${product.code}</td>
                <td>${product.name}</td>
                <td>${product.cost_price}</td>
                <td>${product.sale_price}</td>
                <td>${product.stock}</td>
                <td><button onclick="deleteProduct(${product.id})">Eliminar</button></td>
            `;
            tableBody.appendChild(row);
        });
    } catch (error) {
        showAlert("error", error.message);
    }
}

async function deleteProduct(productId) {
    try {
        const response = await fetch(`/api/products/${productId}`, { method: "DELETE" });
        if (!response.ok) {
            throw new Error("No se pudo eliminar el producto.");
        }

        showAlert("success", "Producto eliminado exitosamente.");
        fetchProducts(); // Actualizar la lista de productos
    } catch (error) {
        showAlert("error", error.message);
    }
}