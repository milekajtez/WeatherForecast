import React from 'react';
import { Route, Routes } from 'react-router-dom';
import { ImportData } from '../ImportData/ImportData';
import { DisplayWeatherData } from '../DisplayResults/DisplayWeatherData';
import { DisplayLoadData } from '../DisplayResults/DisplayLoadData';
import { Training } from '../Training/Training';
import Home from '../Home/Home';

export function Routing() {
  return (
    <div className="container">
      <Routes>
        <Route path={'/'} exact element={<Home />} />
        <Route path={'/importData'} element={<ImportData />} />
        <Route path={'/displayWeatherData'} exact element={<DisplayWeatherData />} />
        <Route path={'/displayLoadData'} exact element={<DisplayLoadData />} />
        <Route path={'/training'} exact element={<Training />} />
      </Routes>
    </div>
  );
}
