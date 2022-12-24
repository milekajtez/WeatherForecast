import React, { useEffect, useState } from 'react';
import '../../css/DisplayCSVFiles.css';
import API from '../../api';

export function DisplayCSVFiles() {
  const [CSVNames, setCSVNames] = useState([]);

  useEffect(() => {
    API.get('/importFiles/loadCSVNames').then((response) => {
      setCSVNames(response.data);
    });
  }, []);

  return (
    <section>
      <div className="tbl-header">
        <table cellPadding="0" cellSpacing="0" border="0">
          <thead>
            <tr>
              <th>NAMES OF ALL CSV FILES</th>
            </tr>
          </thead>
        </table>
      </div>
      <div className="tbl-content">
        <table cellPadding="0" cellSpacing="0" border="0">
          <tbody>
            {CSVNames.map((item, index) => {
              return (
                <tr key={index}>
                  <td>{item}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </section>
  );
}