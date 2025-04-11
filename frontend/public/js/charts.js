import Chart from 'chart.js/auto';

const ctx = document.getElementById('myChart').getContext('2d');
const myChart = new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['Producto A', 'Producto B', 'Producto C'],
        datasets: [{
            label: 'Ventas',
            data: [12, 19, 3],
            backgroundColor: ['rgba(255, 99, 132, 0.2)'],
            borderColor: ['rgba(255, 99, 132, 1)'],
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
    }
});