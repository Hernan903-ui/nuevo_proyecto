// reports.js

// Generar gráficos con Chart.js
async function generateSalesReport() {
    try {
        const response = await fetch('/reports/sales-analysis');
        const data = await response.json();

        const ctx = document.getElementById('salesChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Más vendido', 'Menos vendido'],
                datasets: [{
                    label: 'Cantidad',
                    data: [data.most_sold.stock, data.least_sold.stock],
                    backgroundColor: ['#4caf50', '#f44336']
                }]
            }
        });
    } catch (error) {
        console.error('Error:', error);
    }
}

// reports.js

// Generar gráfico de productos más vendidos
async function generateMostSoldReport() {
    try {
        const response = await fetch('/reports/most-sold');
        const data = await response.json();

        const labels = data.map(item => item.name);
        const values = data.map(item => item.total_sold);

        const ctx = document.getElementById('mostSoldChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels,
                datasets: [{
                    label: 'Cantidad Vendida',
                    data: values,
                    backgroundColor: '#4caf50',
                }]
            }
        });
    } catch (error) {
        console.error('Error al generar el reporte de productos más vendidos:', error);
    }
}

// Generar gráfico de productos más rentables
async function generateMostProfitableReport() {
    try {
        const response = await fetch('/reports/most-profitable');
        const data = await response.json();

        const labels = data.map(item => item.name);
        const values = data.map(item => item.total_profit);

        const ctx = document.getElementById('mostProfitableChart').getContext('2d');
        new Chart(ctx, {
            type: 'bar',
            data: {
                labels,
                datasets: [{
                    label: 'Ganancia Total',
                    data: values,
                    backgroundColor: '#f57c00',
                }]
            }
        });
    } catch (error) {
        console.error('Error al generar el reporte de productos más rentables:', error);
    }
}

// Llamar a las funciones al cargar la página
window.onload = () => {
    generateMostSoldReport();
    generateMostProfitableReport();
};

// Descargar reporte PDF
async function downloadPDF() {
    try {
        const response = await fetch('/reports/generate-pdf');
        const blob = await response.blob();

        const link = document.createElement('a');
        link.href = window.URL.createObjectURL(blob);
        link.download = 'reporte_inventario.pdf';
        link.click();
    } catch (error) {
        console.error('Error:', error);
    }
}