import React, { useEffect, useState } from 'react';
import { Navbar } from '../Navbar/Navbar';
import API from '../../api';
import { WeatherResults } from './WeatherResults';
import '../../css/DisplayCSVFiles.css';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export const options = {
  responsive: true,
  interaction: {
    mode: 'index',
    intersect: false
  },
  stacked: false,
  plugins: {
    title: {
      display: true,
      text: 'Temperature average per year'
    }
  },
  scales: {
    y: {
      type: 'linear',
      display: true,
      position: 'left'
    },
    y1: {
      type: 'linear',
      display: true,
      position: 'right',
      grid: {
        drawOnChartArea: false
      }
    }
  }
};

export const labels = ['2018', '2019', '2020', '2021'];

export const data = {
  labels,
  datasets: [
    {
      label: 'Average temperature per year',
      data: [50, 60, 45, 35],
      borderColor: 'rgb(255, 99, 132)',
      backgroundColor: 'rgba(255, 99, 132, 0.5)',
      yAxisID: 'y'
    },
    {
      label: 'Average load per year',
      data: [350, 450, 83, 400],
      borderColor: 'blue',
      backgroundColor: 'aqua',
      yAxisID: 'y'
    }
  ]
};

export function DisplayImportedData() {
  const [weatherData, setWeatherData] = useState([]);

  useEffect(() => {
    API.get('/loadDataForDisplay?load_type=weather').then((response) => {
      console.log(response.data);
      setWeatherData(response.data);
    });
  }, []);

  return (
    <>
      {weatherData.length > 0 ? (
        <>
          <WeatherResults weatherData={weatherData} />
          <br></br>
          <div style={{ backgroundColor: 'black', display: 'inline-block', width: '500px' }}>
            <Line options={options} data={data} />
          </div>
        </>
      ) : (
        <div className="loader">
          <div style={{ color: 'white' }}>LOAD WEATHER DATA ...</div>
        </div>
      )}
      <Navbar pageName="DISPLAY IMPORTED DATA" />
    </>
  );
}
