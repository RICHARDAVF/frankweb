function generateData() {
  const labels = ['Manzanas', 'Naranjas', 'Plátanos'];
  const values = [Math.random(), Math.random(), Math.random()];
  return { labels, values };
}

const { labels, values } = generateData();
const data = [{ values, labels, type: 'pie' }];
const layout = { height: 400, width: 400 };
Plotly.newPlot('my-pie-chart', data, layout);

const { xValues1, yValues1 } = generateData();
const data1 = [{ x: xValues1, y: yValues1, type: 'bar' }];
const layout1 = { height: 400, width: 400 };
Plotly.newPlot('my-bar-chart', data1, layout1);