document.addEventListener('DOMContentLoaded', () => {
    // Gráfico de Ventas Totales
    Highcharts.chart('total-sales-chart', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Ventas Totales'
        },
        xAxis: {
            categories: ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo']
        },
        yAxis: {
            title: {
                text: 'Monto ($)'
            }
        },
        series: [{
            name: 'Ventas',
            data: [5000, 7000, 8000, 12000, 15000] // Datos de ejemplo
        }]
    });

    // Gráfico de Productos Más Vendidos
    Highcharts.chart('best-sellers-chart', {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Productos Más Vendidos'
        },
        series: [{
            name: 'Ventas',
            data: [
                { name: 'Producto A', y: 40 },
                { name: 'Producto B', y: 30 },
                { name: 'Producto C', y: 20 },
                { name: 'Producto D', y: 10 }
            ]
        }]
    });
});
fetch('/api/dashboard-data')
    .then(response => response.json())
    .then(data => {
        Highcharts.chart('total-sales-chart', {
            // Configuración del gráfico...
            series: [{
                name: 'Ventas',
                data: data.totalSales
            }]
        });

        Highcharts.chart('best-sellers-chart', {
            // Configuración del gráfico...
            series: [{
                name: 'Ventas',
                data: data.bestSellers
            }]
        });
    });