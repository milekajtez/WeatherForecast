import './App.css';
import Home from './components/Home/Home';
import { Route, Routes } from 'react-router-dom';
import { ImportData } from './components/ImportData/ImportData';
import { Trening } from './components/Trening/Trening';
import { Forecast } from './components/Forecast/Forecast';
import { DisplayResults } from './components/DisplayResults/DisplayResults';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path={'/'} exact element={<Home />} />
        <Route path={'/importData'} element={<ImportData />} />
        <Route path={'/trening'} exact element={<Trening />} />
        <Route path={'/forecast'} exact element={<Forecast />} />
        <Route path={'/displayResults'} exact element={<DisplayResults />} />
      </Routes>
    </div>
  );
}

export default App;
