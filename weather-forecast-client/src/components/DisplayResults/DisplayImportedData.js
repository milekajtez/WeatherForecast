import React, { useEffect, useState } from 'react';
import { Navbar } from '../Navbar/Navbar';
import API from '../../api';
import '../../css/DisplayCSVFiles.css';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  BarElement
} from 'chart.js';
import { Bar, Line } from 'react-chartjs-2';
import {
  dataPerYear,
  getLineChartOptions,
  temperatureData,
  temperaturePerMonthsData
} from '../../Helpers/ChartHelper';

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export function DisplayImportedData() {
  const [averageTemperatureData, setAverageTemperatureData] = useState([]);
  const [conditions2018, setConditions2018] = useState([]);
  const [conditions2019, setConditions2019] = useState([]);
  const [conditions2020, setConditions2020] = useState([]);
  const [conditions2021, setConditions2021] = useState([]);
  const [monthsTemp2018, setMonthsTemp2018] = useState([]);
  const [monthsTemp2019, setMonthsTemp2019] = useState([]);
  const [monthsTemp2020, setMonthsTemp2020] = useState([]);
  const [monthsTemp2021, setMonthsTemp2021] = useState([]);
  const [loadsTemp2018, setLoadsTemp2018] = useState([]);
  const [loadsTemp2019, setLoadsTemp2019] = useState([]);
  const [loadsTemp2020, setLoadsTemp2020] = useState([]);
  const [loadsTemp2021, setLoadsTemp2021] = useState([]);

  useEffect(() => {
    API.get('/averageTemperaturesPerYears').then((response) => {
      setAverageTemperatureData(response.data);
    });

    API.get('/getNumberOfDaysWithSpecificConditionsPerYear?year=2018').then((response) => {
      setConditions2018(response.data);
    });

    API.get('/getNumberOfDaysWithSpecificConditionsPerYear?year=2019').then((response) => {
      setConditions2019(response.data);
    });

    API.get('/getNumberOfDaysWithSpecificConditionsPerYear?year=2020').then((response) => {
      setConditions2020(response.data);
    });

    API.get('/getNumberOfDaysWithSpecificConditionsPerYear?year=2021').then((response) => {
      setConditions2021(response.data);
    });

    API.get('/getMonthsTemperature').then((response) => {
      setMonthsTemp2018(response.data.y2018);
      setMonthsTemp2019(response.data.y2019);
      setMonthsTemp2020(response.data.y2020);
      setMonthsTemp2021(response.data.y2021);
    });

    API.get('/getMonthsLoads').then((response) => {
      setLoadsTemp2018(response.data.y2018);
      setLoadsTemp2019(response.data.y2019);
      setLoadsTemp2020(response.data.y2020);
      setLoadsTemp2021(response.data.y2021);
    });
  }, []);

  return (
    <>
      <div style={{ display: 'inline-flex', marginTop: '70px' }}>
        <span style={{ backgroundColor: 'black', width: '500px', margin: '15px' }}>
          <Line
            options={getLineChartOptions('Temperature average per year [F - fahrenheit]')}
            data={temperatureData(averageTemperatureData)}
          />
        </span>
        <span style={{ backgroundColor: 'black', width: '500px', margin: '15px' }}>
          <Bar options={getLineChartOptions('Conditions [%]')} data={dataPerYear(conditions2018)} />
        </span>
        <span style={{ backgroundColor: 'black', width: '500px', margin: '15px' }}>
          <Bar options={getLineChartOptions('Conditions [%]')} data={dataPerYear(conditions2019)} />
        </span>
      </div>
      <div style={{ display: 'inline-flex', marginTop: '70px' }}>
        <span style={{ backgroundColor: 'black', width: '500px', margin: '15px' }}>
          <Bar options={getLineChartOptions('Conditions [%]')} data={dataPerYear(conditions2020)} />
        </span>
        <span style={{ backgroundColor: 'black', width: '500px', margin: '15px' }}>
          <Bar options={getLineChartOptions('Conditions [%]')} data={dataPerYear(conditions2021)} />
        </span>
      </div>

      <div style={{ display: 'inline-flex', marginTop: '70px' }}>
        <span style={{ backgroundColor: 'black', width: '500px', margin: '15px' }}>
          <Line
            options={getLineChartOptions('Temperature pre month (years)  [F - fahrenheit]')}
            data={temperaturePerMonthsData(
              monthsTemp2018,
              monthsTemp2019,
              monthsTemp2020,
              monthsTemp2021
            )}
          />
        </span>
        <span style={{ backgroundColor: 'black', width: '500px', margin: '15px' }}>
          <Line
            options={getLineChartOptions('Load pre month (years)')}
            data={temperaturePerMonthsData(
              loadsTemp2018,
              loadsTemp2019,
              loadsTemp2020,
              loadsTemp2021
            )}
          />
        </span>
      </div>
      <Navbar pageName="DISPLAY IMPORTED DATA" />
    </>
  );
}
