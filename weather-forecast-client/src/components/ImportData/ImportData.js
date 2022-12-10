import React from 'react';
import { Navbar } from '../Navbar/Navbar';
import { DisplayCSVFiles } from './DisplayCSVFiles';
import '../../css/ImportData.css';
import API from '../../api';

export function ImportData() {
  const handleImportData = () => {
    API.get('/importFiles').then((response) => {
      console.log(response.data);
      alert('Import data successfully. You can start training model.');
    });
  };
  return (
    <>
      <Navbar pageName="IMPORT DATA" />
      <DisplayCSVFiles />
      <button className="button aqua" onClick={() => handleImportData()}>
        <div className="glare"></div>
        IMPORT DATA FROM CSV FILES AND SAVE TO MONGODB
      </button>
    </>
  );
}
