import React, { useEffect, useState } from 'react';
import { DisplayCSVFiles } from './DisplayCSVFiles';
import '../../css/ImportDataStyles.css';
import API from '../../api';
import { Loader } from '../../Helpers/Loader';

export function ImportData() {
  const [loader, setLoader] = useState(false);
  const [disableImportData, setDisableImportData] = useState(false);

  useEffect(() => {
    API.get('importData/checkDoesDataExists').then((response) => {
      setDisableImportData(response.data);
    });
  }, []);

  const handleImportData = () => {
    setLoader(true);
    API.post('/importData/processCsvData').then((response) => {
      setLoader(false);
      alert(response.data);
    });
  };

  return (
    <div className="importData">
      <DisplayCSVFiles />
      <Loader loader={loader} />
      <button
        disabled={disableImportData}
        className="import-button linear-aqua"
        onClick={() => handleImportData()}
        title="This action is enable only if yout don't have imported data in data-base">
        Import data from csv files to mongo database
      </button>
    </div>
  );
}
