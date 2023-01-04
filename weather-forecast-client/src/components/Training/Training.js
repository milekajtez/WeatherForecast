import React, { useState } from 'react';
import 'react-datepicker/dist/react-datepicker.css';
import DatePicker from 'react-datepicker';
import '../../css/DisplayOtherWeatherDataStyles.css';
import { trainingPercetages, trainingValidation } from '../../Helpers/Training';
import '../../css/Training.css';
import API from '../../api';
import { Loader } from '../../Helpers/Loader';

export function Training() {
  const [loader, setLoader] = useState(false);
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());
  const [percentForTraining, setPercentForTraining] = useState(-1);

  const setStartDateHandler = (date) => {
    setStartDate(date);
  };

  const setEndDateHandler = (date) => {
    setEndDate(date);
  };

  const setPercentOption = (option) => {
    setPercentForTraining(option);
  };

  const training = () => {
    if (!trainingValidation(startDate, endDate, percentForTraining)) {
      alert('Please insert valid parameters for training');
      return;
    }

    setLoader(true);
    var start = startDate.toISOString().split('T')[0];
    var end = endDate.toISOString().split('T')[0];

    API.post(`/training/trainingModel?start=${start}&end=${end}&option=${percentForTraining}`).then(
      (response) => {
        setLoader(false);
        alert(response.data);
      }
    );
  };

  return (
    <div className="container">
      <Loader loader={loader} text="TRAINING MODEL..." />
      <h2 className="welcome-title">Here you can make and training your model for prediction</h2>
      <div className="welcome-text">
        First you have to fill in the time range for which the data for turning will be taken. Then
        enter how much data you want to use for training (50% - 90%). The rest of the data will be
        used for model testing.
      </div>
      <hr></hr>
      <h3 className="welcome-title">Define date range</h3>
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
      <h3 className="welcome-title">Select Percent for training</h3>
      <select
        className="custom-select"
        style={{ width: '200px' }}
        defaultValue={'Please select option'}
        onChange={(e) => setPercentOption(e.target.value)}>
        <option value={''}>Select training percantage</option>
        {trainingPercetages.map((item, index) => {
          return (
            <option key={index} value={item}>
              {item}%
            </option>
          );
        })}
      </select>
      <br></br>
      <button className="import-button linear-aqua" onClick={() => training()}>
        Training
      </button>
    </div>
  );
}
