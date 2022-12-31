import React from 'react';
import '../../css/HomeStyles.css';
import homegif from '../../images/home.gif';

export default function Home() {
  return (
    <div className="container">
      <h1 className="welcome-title">Welcome to forecast application!</h1>
      <div className="welcome-text">
        The application enables displaying the names of data files, import data from CSV files and
        place them in data-base, displaying loaded and weather data, creation of neural network
        models, prediction of electricity consumption based on weather conditions and so on...
      </div>
      <img src={homegif}></img>
    </div>
  );
}
