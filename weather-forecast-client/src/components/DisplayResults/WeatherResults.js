import React from 'react';
import '../../css/ImportData.css';

export function WeatherResults(props) {
  const { weatherData } = props;

  console.log(weatherData);

  return (
    <>
      <section style={{ marginTop: '100px' }}>
        <div style={{ color: 'white', margin: '5px', fontSize: '20px' }}>WEATHER DATA</div>
        <div>
          <table cellPadding="0" cellSpacing="0" border="0">
            <thead>
              <tr>
                <th>DATE TIME</th>
                <th>TEMPERATURE</th>
                <th>SNOW</th>
                <th>WIND SPEED</th>
                <th>CLOUD COVER</th>
                <th>CONDITION</th>
              </tr>
            </thead>
          </table>
        </div>
        <div className="tbl-content">
          <table cellPadding="0" cellSpacing="0" border="0">
            <tbody>
              {weatherData.map((item, index) => {
                return (
                  <tr key={index}>
                    <td>{item.datetime}</td>
                    <td>{item.temp} F</td>
                    <td>{item.snow} %</td>
                    <td>{item.windspeed} km/h</td>
                    <td>{item.cloudcover} %</td>
                    <td>{item.conditions}</td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </section>
    </>
  );
}
