import React, { useState } from 'react';
import { DisplayCSVFiles } from './DisplayCSVFiles';
import '../../css/ImportData.css';
import API from '../../api';
import { Loader } from '../../Helpers/Loader';

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
    <div className="importData">
      <DisplayCSVFiles />
      <Loader loader={loader} />
      <button className="button aqua" onClick={() => handleImportData()}>
        <div className="glare"></div>
        Import data from csv files to mongo database
      </button>
    </div>
  );
}
