import styled from 'styled-components';

export const years = ['2018', '2019', '2020', '2021'];
export const conditions = [
  'Clear',
  'Partially cloudy',
  'Overcast',
  'Rain',
  'Rain, Partially cloudy',
  'Rain, Overcast',
  'Snow, Partially cloudy',
  'Snow, Overcast',
  'Snow'
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
          'rgb(255, 99, 132, 0.5)',
          'rgb(255, 0, 0, 0.5)',
          'rgb(0, 102, 102, 0.5)',
          'rgb(0, 153, 0, 0.5)',
          'rgb(255, 189, 0, 0.5)',
          'rgba(153, 102, 255, 0.5)',
          'rgba(201, 203, 207, 0.5)',
          'rgba(0, 0, 0, 0.5)',
          'rgba(110, 197, 232, 0.5)'
        ],
        borderColor: [
          'rgb(255, 99, 132)',
          'rgb(255, 0, 0)',
          'rgb(0, 102, 102)',
          'rgb(0, 153, 0)',
          'rgb(255, 189, 0)',
          'rgba(153, 102, 255)',
          'rgba(201, 203, 207)',
          'rgba(0, 0, 0, 1)',
          'rgba(110, 197, 232, 1)'
        ],
        borderWidth: 2
      }
    ]
  };
};

export const dataPerMonthsData = (
  temperatures2018,
  temperatures2019,
  temperatures2020,
  temperatures2021,
  text
) => {
  return {
    labels: months,
    datasets: [
      {
        label: `${text} - Year 2018`,
        data: temperatures2018,
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        yAxisID: 'y'
      },
      {
        label: `${text} - Year 2019`,
        data: temperatures2019,
        borderColor: 'rgb(255, 189, 0)',
        backgroundColor: 'rgb(207, 189, 146)',
        yAxisID: 'y'
      },
      {
        label: `${text} - Year 2020`,
        data: temperatures2020,
        borderColor: 'rgb(0, 102, 102)',
        backgroundColor: 'rgb(0, 255, 255)',
        yAxisID: 'y'
      },
      {
        label: `${text} - Year 2021`,
        data: temperatures2021,
        borderColor: 'rgb(0, 153, 0)',
        backgroundColor: 'rgb(153, 204, 0)',
        yAxisID: 'y'
      }
    ]
  };
};

export const otherWeatherDataPerMonthsData = (
  windSpeed,
  cloudCover,
  snow,
  windSpeedText,
  cloudCoverText,
  snowText
) => {
  return {
    labels: months,
    datasets: [
      {
        label: windSpeedText,
        data: windSpeed,
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        yAxisID: 'y'
      },
      {
        label: cloudCoverText,
        data: cloudCover,
        borderColor: 'rgb(255, 189, 0)',
        backgroundColor: 'rgb(207, 189, 146)',
        yAxisID: 'y'
      },
      {
        label: snowText,
        data: snow,
        borderColor: 'rgb(0, 102, 102)',
        backgroundColor: 'rgb(0, 255, 255)',
        yAxisID: 'y'
      }
    ]
  };
};

export const loadAndTempPerMonthsData = (loads, temperatures, loadText, temperatureText, dates) => {
  return {
    labels: dates,
    datasets: [
      {
        label: loadText,
        data: loads,
        borderColor: 'rgb(255, 99, 132)',
        backgroundColor: 'rgba(255, 99, 132, 0.5)',
        yAxisID: 'y'
      },
      {
        label: temperatureText,
        data: temperatures,
        borderColor: 'rgb(0, 102, 102)',
        backgroundColor: 'rgb(0, 255, 255)',
        yAxisID: 'y'
      }
    ]
  };
};

export const ChartWrapper = styled.div`
  display: inline-flex;
  background: 'linear-gradient(to right, #25c481, #25b7c4)';
`;

export const ChartCanvasWrapper = styled.span`
  border: '1px solid black;
  margin: 10px;
`;

export const chartStyle = () => {
  return { background: 'linear-gradient(to right, #25c481, #25b7c4)', margin: '10px' };
};
