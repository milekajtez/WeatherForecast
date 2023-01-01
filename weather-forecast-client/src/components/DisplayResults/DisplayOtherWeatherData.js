import React, { useState } from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  BarElement,
  Colors
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import API from '../../api';
import {
  ChartCanvasWrapper,
  chartStyle,
  ChartWrapper,
  otherWeatherDataPerMonthsData,
  getLineChartOptions,
  years
} from '../../Helpers/ChartHelper';
import '../../css/DisplayOtherWeatherDataStyles.css';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend,
  Colors
);

export function DisplayOtherWeatherData() {
  const [yearOption, setYearOption] = useState('');
  const [windSpeed, setWindSpeed] = useState([]);
  const [cloudCover, setCloudCover] = useState([]);
  const [snow, setSnow] = useState([]);

  const getOtherWeatherDataPerYear = (year) => {
    setYearOption(year);
    if (year != '') {
      API.get(`/displayWeatherData/getOtherWeatherData?year=${year}`).then((response) => {
        setWindSpeed(response.data.windSpeed);
        setCloudCover(response.data.cloudCover);
        setSnow(response.data.snow);
      });
    }
  };

  const displayChart = () => {
    return (
      <ChartWrapper>
        <ChartCanvasWrapper>
          <Line
            height="400px"
            width="600px"
            options={getLineChartOptions('Other weather parameters per year  [F - fahrenheit]')}
            data={otherWeatherDataPerMonthsData(
              windSpeed,
              cloudCover,
              snow,
              'Days with wind',
              'Days with clouds',
              'Days with snow'
            )}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
      </ChartWrapper>
    );
  };

  return (
    <>
      <h3 className="welcome-title">Other weather data</h3>
      <select
        className="custom-select"
        style={{ width: '200px' }}
        defaultValue={'Please select option'}
        onChange={(e) => getOtherWeatherDataPerYear(e.target.value)}>
        <option value={''}>Cancel current graphic</option>
        {years.map((item, index) => {
          return (
            <option key={index} value={item}>
              {item}
            </option>
          );
        })}
      </select>
      <br></br>
      {yearOption != '' ? displayChart() : null}
    </>
  );
}
