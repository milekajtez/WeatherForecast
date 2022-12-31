import React, { useEffect, useState } from 'react';
import API from '../../api';
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
import { Bar, Line } from 'react-chartjs-2';
import {
  chartStyle,
  ChartWrapper,
  ChartCanvasWrapper,
  dataPerYear,
  getLineChartOptions,
  temperatureData,
  dataPerMonthsData
} from '../../Helpers/ChartHelper';

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

export function DisplayWeatherData() {
  const [averageTemperatureData, setAverageTemperatureData] = useState([]);
  const [conditions2018, setConditions2018] = useState([]);
  const [conditions2019, setConditions2019] = useState([]);
  const [conditions2020, setConditions2020] = useState([]);
  const [conditions2021, setConditions2021] = useState([]);
  const [monthsTemp2018, setMonthsTemp2018] = useState([]);
  const [monthsTemp2019, setMonthsTemp2019] = useState([]);
  const [monthsTemp2020, setMonthsTemp2020] = useState([]);
  const [monthsTemp2021, setMonthsTemp2021] = useState([]);

  useEffect(() => {
    API.get('/displayWeatherData/averageTemperaturesPerYear').then((response) => {
      setAverageTemperatureData(response.data);
    });

    API.get('/displayWeatherData/getConditionsPerYear?year=2018').then((response) => {
      setConditions2018(response.data);
    });

    API.get('/displayWeatherData/getConditionsPerYear?year=2019').then((response) => {
      setConditions2019(response.data);
    });

    API.get('/displayWeatherData/getConditionsPerYear?year=2020').then((response) => {
      setConditions2020(response.data);
    });

    API.get('/displayWeatherData/getConditionsPerYear?year=2021').then((response) => {
      setConditions2021(response.data);
    });

    API.get('/displayWeatherData/getTemperaturePerMonth').then((response) => {
      setMonthsTemp2018(response.data.y2018);
      setMonthsTemp2019(response.data.y2019);
      setMonthsTemp2020(response.data.y2020);
      setMonthsTemp2021(response.data.y2021);
    });
  }, []);
  return (
    <>
      <ChartWrapper>
        <ChartCanvasWrapper>
          <Line
            height="400px"
            width="600px"
            options={getLineChartOptions('Temperature average per year [F - fahrenheit]')}
            data={temperatureData(averageTemperatureData)}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
        <ChartCanvasWrapper>
          <Bar
            height="400px"
            width="600px"
            options={getLineChartOptions('Conditions [%]')}
            data={dataPerYear(conditions2018)}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
        <ChartCanvasWrapper>
          <Bar
            height="400px"
            width="600px"
            options={getLineChartOptions('Conditions [%]')}
            data={dataPerYear(conditions2019)}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
      </ChartWrapper>
      <ChartWrapper>
        <ChartCanvasWrapper>
          <Bar
            height="400px"
            width="600px"
            options={getLineChartOptions('Conditions [%]')}
            data={dataPerYear(conditions2020)}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
        <ChartCanvasWrapper>
          <Bar
            height="400px"
            width="600px"
            options={getLineChartOptions('Conditions [%]')}
            data={dataPerYear(conditions2021)}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
        <ChartCanvasWrapper>
          <Line
            height="400px"
            width="600px"
            options={getLineChartOptions('Temperature per month (years)  [F - fahrenheit]')}
            data={dataPerMonthsData(
              monthsTemp2018,
              monthsTemp2019,
              monthsTemp2020,
              monthsTemp2021,
              'Temperature'
            )}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
      </ChartWrapper>
    </>
  );
}
