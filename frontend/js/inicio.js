const ctx = document.getElementById('dona-grafica').getContext('2d');


const data = {
    labels: ['Completado',  'Faltantes'],
    datasets: [{
        data: [300, 50],
        backgroundColor: [
            'rgb(239, 118, 122)',
            'rgb(255, 205, 86)'
        ],
        hoverOffset: 4
    }]
};

const config = {
    type: 'doughnut',
    data: data,
    options: {
        responsive: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
            }
        }
    }
};

const myDoughnutChart = new Chart(ctx, config);