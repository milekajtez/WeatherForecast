import React, { useState } from 'react';
import { Navbar } from '../Navbar/Navbar';
import { DisplayCSVFiles } from './DisplayCSVFiles';
import '../../css/ImportData.css';
import API from '../../api';

export function ImportData() {
  const [loader, setLoader] = useState(false);
  const handleImportData = () => {
    setLoader(true);
    API.post('/importDataFromCSV').then((response) => {
      console.log(response.data);
      setLoader(false);
      alert("Import data from csv successfully. See 'Display data' page to see all imported data");
    });
  };

  return (
    <>
      <Navbar pageName="IMPORT DATA" />
      <DisplayCSVFiles />
      {loader == true ? (
        <div className="loader">
          <div style={{ color: 'white' }}>IMPORTING DATA FROM CSV ...</div>
        </div>
      ) : null}
      <button className="button aqua" onClick={() => handleImportData()}>
        <div className="glare"></div>
        IMPORT DATA FROM CSV FILES AND SAVE TO MONGODB
      </button>
    </>
  );
}
