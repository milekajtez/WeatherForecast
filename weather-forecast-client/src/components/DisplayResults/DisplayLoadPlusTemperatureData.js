import React, { useState } from 'react';
import API from '../../api';
import {
  Chart as ChartJS,
  CategoryScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
  BarElement,
  Colors
} from 'chart.js';
import { Line } from 'react-chartjs-2';
import {
  ChartCanvasWrapper,
  chartStyle,
  ChartWrapper,
  getLineChartOptions,
  loadAndTempPerMonthsData
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
import 'react-datepicker/dist/react-datepicker.css';
import DatePicker from 'react-datepicker';
import '../../css/DisplayOtherWeatherDataStyles.css';

export function DisplayLoadPlusTemperatureData() {
  const [buttonClicked, setButtonClicked] = useState(false);
  const [loadData, setLoadData] = useState([]);
  const [tempData, setTempData] = useState([]);
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());

  const [dates, setDates] = useState([]);
  const setStartDateHandler = (date) => {
    setStartDate(date);
  };

  const setEndDateHandler = (date) => {
    setEndDate(date);
  };

  const calculateData = (data) => {
    var datesTextList = [];
    var values = [];
    values.push(0);

    var counters = [];
    counters.push(1);

    var currentDate = data[0].date;

    data.forEach((data) => {
      if (currentDate.split(' ')[0] === data.date.split(' ')[0]) {
        values[values.length - 1] += data.value;
        counters[counters.length - 1] += 1;
      } else {
        values.push(data.value);
        counters.push(1);
        currentDate = data.date;
        datesTextList.push(data.date);
      }
    });

    var result = [];
    for (let i = 0; i < values.length; i++) {
      result.push(values[i] / counters[i]);
    }

    setDates(datesTextList);
    return result;
  };

  const getLoadPlusTempDataHandler = () => {
    var start = startDate.toISOString().split('T')[0];
    var end = endDate.toISOString().split('T')[0];
    API.get(`/displayLoadData/getLoadsAndTemperature?start=${start}&end=${end}`).then(
      (response) => {
        if (response.data.loads.length === 0 && response.data.temperatures.length === 0) {
          alert("For entered range we don't have any data");
          setButtonClicked(false);
        } else {
          setButtonClicked(true);
          setLoadData(calculateData(response.data.loads));
          setTempData(calculateData(response.data.temperatures));
        }
      }
    );
  };

  const displayChart = () => {
    return (
      <ChartWrapper>
        <ChartCanvasWrapper style={{ width: '1500px' }}>
          <Line
            height="800px"
            width="1200px"
            options={getLineChartOptions('Load + temperature')}
            data={loadAndTempPerMonthsData(
              loadData,
              tempData,
              'Load values',
              'Temperature values',
              dates
            )}
            style={chartStyle()}
          />
        </ChartCanvasWrapper>
      </ChartWrapper>
    );
  };

  return (
    <>
      <h3 className="welcome-title">Load plus temperature values</h3>
      <div className="datepicker-wrapper">
        <DatePicker
          className="datePicker"
          selected={startDate}
          onChange={(date) => setStartDateHandler(date)}
          format="yyyy-dd-MM"
        />
        <DatePicker
          className="datePicker"
          selected={endDate}
          onChange={(date) => setEndDateHandler(date)}
          format="yyyy-dd-MM"
        />
      </div>
      <br></br>
      <button className="import-button linear-aqua" onClick={() => getLoadPlusTempDataHandler()}>
        Send request
      </button>
      <br></br>
      {buttonClicked ? displayChart() : null}
    </>
  );
}
