export const years = ['2018', '2019', '2020', '2021'];
export const conditions = [
  'Clear',
  'Partially cloudy',
  'Overcast',
  'Rain, Partially cloudy',
  'Rain, Overcast',
  'Snow, Partially cloudy',
  'Snow, Overcast'
];
export const months = [
  'January',
  'February',
  'March',
  'April',
  'May',
  'June',
  'July',
  'August',
  'September',
  'October',
  'November',
  'December'
];

export const getLineChartOptions = (title) => {
  return {
    responsive: true,
    interaction: {
      mode: 'index',
      intersect: false
    },
    stacked: false,
    plugins: {
      title: {
        display: true,
        text: title
      }
    },
    scales: {
      y: {
        type: 'linear',
        display: true,
        position: 'left'
      }
    }
  };
};

export const getBarChartOptions = (condition) => {
  return {
    type: 'bar',
    data: condition,
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      }
    }
  };
};

export const temperatureData = (temperature) => {
  return {
    labels: years,
    datasets: [
      {
        label: 'Average temperature per year',
        data: temperature,
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        yAxisID: 'y'
      }
    ]
  };
};

export const dataPerYear = (dataYear) => {
  return {
    labels: conditions,
    datasets: [
      {
        label: 'Conditions',
        data: dataYear,
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 205, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(201, 203, 207, 0.2)'
        ],
        borderColor: [
          'rgb(255, 99, 132)',
          'rgb(255, 159, 64)',
          'rgb(255, 205, 86)',
          'rgb(75, 192, 192)',
          'rgb(54, 162, 235)',
          'rgb(153, 102, 255)',
          'rgb(201, 203, 207)'
        ],
        borderWidth: 1
      }
    ]
  };
};

export const temperaturePerMonthsData = (
  temperatures2018,
  temperatures2019,
  temperatures2020,
  temperatures2021
) => {
  return {
    labels: months,
    datasets: [
      {
        label: 'Temperature - Year 2018',
        data: temperatures2018,
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        yAxisID: 'y'
      },
      {
        label: 'Temperature - Year 2019',
        data: temperatures2019,
        borderColor: 'rgb(255, 189, 0)',
        backgroundColor: 'rgb(207, 189, 146)',
        yAxisID: 'y'
      },
      {
        label: 'Temperature - Year 2020',
        data: temperatures2020,
        borderColor: 'rgb(0, 102, 102)',
        backgroundColor: 'rgb(0, 255, 255)',
        yAxisID: 'y'
      },
      {
        label: 'Temperature - Year 2021',
        data: temperatures2021,
        borderColor: 'rgb(0, 153, 0)',
        backgroundColor: 'rgb(153, 204, 0)',
        yAxisID: 'y'
      }
    ]
  };
};
