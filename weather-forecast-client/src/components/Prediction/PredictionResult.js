import React from 'react';

export function PredictionResult(props) {
  const { predictResults, predictDatetimes } = props;

  const concatData = () => {
    var result = [];
    for (let i = 0; i < predictResults.length; i++) {
      result.push({
        datetime: predictDatetimes[i],
        load: predictResults[i]
      });
    }

    return result;
  };

  return (
    <div style={{ marginLeft: '30%', marginRight: '30%', paddingBottom: '20px' }}>
      <br></br>
      <table cellPadding="0" cellSpacing="0" border="0">
        <thead>
          <tr>
            <th>Here you can see predicted load data</th>
          </tr>
        </thead>
      </table>
      <div className="tbl-content">
        <table cellPadding="0" cellSpacing="0" border="0">
          <thead>
            <th>Date time</th>
            <th>Load value</th>
          </thead>
          <tbody>
            {concatData().map((item, index) => {
              return (
                <tr key={index}>
                  <td>{item.datetime}</td>
                  <td>{item.load}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
}
