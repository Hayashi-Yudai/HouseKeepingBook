var ctx = document.getElementById("data").getContext("2d");
ctx.canvas.width = 400;
ctx.canvas.height = 270;
var myChart = new Chart(ctx, json);
