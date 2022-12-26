import './App.css';
import Home from './components/Home/Home';
import { Route, Routes } from 'react-router-dom';
import { ImportData } from './components/ImportData/ImportData';
import { Trening } from './components/Trening/Trening';
import { Forecast } from './components/Forecast/Forecast';
import { DisplayImportedData } from './components/DisplayResults/DisplayImportedData';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path={'/'} exact element={<Home />} />
        <Route path={'/importData'} element={<ImportData />} />
        <Route path={'/trening'} exact element={<Trening />} />
        <Route path={'/forecast'} exact element={<Forecast />} />
        <Route path={'/displayImportedData'} exact element={<DisplayImportedData />} />
      </Routes>
    </div>
  );
}

export default App;
