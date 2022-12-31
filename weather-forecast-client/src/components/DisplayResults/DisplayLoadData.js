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
  BarElement
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import {
  chartStyle,
  ChartWrapper,
  ChartCanvasWrapper,
  getLineChartOptions,
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
  Legend
);

export function DisplayLoadData() {
  const [loadsTemp2018, setLoadsTemp2018] = useState([]);
  const [loadsTemp2019, setLoadsTemp2019] = useState([]);
  const [loadsTemp2020, setLoadsTemp2020] = useState([]);
  const [loadsTemp2021, setLoadsTemp2021] = useState([]);

  useEffect(() => {
    API.get('/displayLoadData/getLoadsPerMonth').then((response) => {
      setLoadsTemp2018(response.data.y2018);
      setLoadsTemp2019(response.data.y2019);
      setLoadsTemp2020(response.data.y2020);
      setLoadsTemp2021(response.data.y2021);
    });
  });
  return (
    <>
      <ChartWrapper>
        <ChartCanvasWrapper>
          <Line
            height="400px"
            width="600px"
            options={getLineChartOptions('Load per month (years)')}
            data={dataPerMonthsData(
              loadsTemp2018,
              loadsTemp2019,
              loadsTemp2020,
              loadsTemp2021,
              'Load'
            )}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
        <ChartCanvasWrapper>
          <Line
            height="400px"
            width="600px"
            options={getLineChartOptions('Load per month (years)')}
            data={dataPerMonthsData(
              loadsTemp2018,
              loadsTemp2019,
              loadsTemp2020,
              loadsTemp2021,
              'Load'
            )}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
        <ChartCanvasWrapper>
          <Line
            height="400px"
            width="600px"
            options={getLineChartOptions('Load per month (years)')}
            data={dataPerMonthsData(
              loadsTemp2018,
              loadsTemp2019,
              loadsTemp2020,
              loadsTemp2021,
              'Load'
            )}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
      </ChartWrapper>
      <ChartWrapper>
        <ChartCanvasWrapper>
          <Line
            height="400px"
            width="600px"
            options={getLineChartOptions('Load per month (years)')}
            data={dataPerMonthsData(
              loadsTemp2018,
              loadsTemp2019,
              loadsTemp2020,
              loadsTemp2021,
              'Load'
            )}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
      </ChartWrapper>
    </>
  );
}
