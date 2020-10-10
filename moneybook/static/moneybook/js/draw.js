let json = {
    type: 'bar',
    data: {
        labels: days,
        datasets: [{
            label: '支出',
            data: payments,
            borderWidth: 2,
            strokeColor: 'rgba(0,0,255,1)',
            backgroundColor: 'rgba(0,191,255,0.5)'
        }]
    },
    options: {
        scales: {
            xAxes: [{
                ticks: {
                    beginAtZero:true
                },
                scaleLabel: {
                    display: true,
                    labelString: '日付',
                    fontsize: 18
                }
            }],
            yAxes: [{
                ticks: {
                    beginAtZero:true
                },
                scaleLabel: {
                    display: true,
                    labelString: '支出額 (円)',
                    fontsize: 18
                }
            }]
        },
        responsive: true
    }
}

var ctx = document.getElementById("data").getContext("2d");
var myChart = new Chart(ctx, json);
