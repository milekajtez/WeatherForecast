import React, { useState } from 'react';
import '../../css/Training.css';
import API from '../../api';
import { Loader } from '../../Helpers/Loader';
import 'react-datepicker/dist/react-datepicker.css';
import DatePicker from 'react-datepicker';
import { predictValidation } from '../../Helpers/Training';
import { PredictionResult } from './PredictionResult';
import axios from 'axios';

export function Prediction() {
  const [loader, setLoader] = useState(false);
  const [startDate, setStartDate] = useState(new Date());
  const [endDate, setEndDate] = useState(new Date());
  const [fileForPrediction, setFileForPrediction] = useState(null);
  const [dateForm, setDateForm] = useState(false);
  const [predictResults, setPredictResults] = useState('');

  const setStartDateHandler = (date) => {
    setStartDate(date);
  };

  const setEndDateHandler = (date) => {
    setEndDate(date);
  };

  const uploadDataForPredictionHandler = (file) => {
    console.log(file.target.files[0]);
    setFileForPrediction(file.target.files[0]);
  };

  const uploadFile = async () => {
    setLoader(true);
    const formData = new FormData();
    formData.append('fileForPrediction', fileForPrediction);

    const response = await axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/prediction/uploadDataForPrediction',
      data: formData,
      headers: { 'Content-Type': 'multipart/form-data' }
    });

    alert(response.data);
    setLoader(false);
    setDateForm(true);
  };

  const predict = () => {
    if (!predictValidation(startDate, endDate)) {
      alert('Please insert valid parameters for training');
      return;
    }

    var start = startDate.toISOString().split('T')[0];
    var end = endDate.toISOString().split('T')[0];

    API.get(`/prediction/predict?start=${start}&end=${end}`).then((response) => {
      alert(response.data);
      setPredictResults(response.data);
    });
  };

  return (
    <div className="container">
      <Loader loader={loader} text="PREDICTION..." />
      <h2 className="welcome-title">Here you can predict load data.</h2>
      <div className="welcome-text">
        First you need to upload weather data. Than you can to choose date range for prediction.
      </div>
      <hr></hr>
      <h3 className="welcome-title">First upload file</h3>
      <br></br>
      <div className="upload-file-wrapper">
        <input type="file" onChange={(e) => uploadDataForPredictionHandler(e)} />
      </div>
      <br></br>
      <button
        disabled={fileForPrediction === null}
        className="import-button linear-aqua"
        onClick={() => uploadFile()}>
        Upload file
      </button>
      <br></br>
      {dateForm === true ? (
        <>
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
          <button
            disabled={fileForPrediction === null}
            className="import-button linear-aqua"
            onClick={() => predict()}>
            Predict
          </button>
        </>
      ) : null}

      {predictResults.length > 0 ? <PredictionResult predictResults={predictResults} /> : null}
    </div>
  );
}
