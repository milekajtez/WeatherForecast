import React from 'react';
import '../../css/Home.css';
import { goToPage } from '../../Helpers/RoutingHelper';
import { useNavigate } from 'react-router-dom';

export default function Home() {
  const navigate = useNavigate();

  return (
    <div className="container">
      <div>
        <p>Welcome to weather forecast application</p>
        <button onClick={() => goToPage('importData', navigate, { replace: true })}>
          Click here to open a menu
        </button>
      </div>

      <div className="popover" id="menu">
        <div className="content">
          <a href="#" className="close"></a>
          <ul className="nav_list">
            <div className="nav_list_item">
              <li>
                <button onClick={() => goToPage('importData', navigate)}>Import data</button>
              </li>
            </div>
            <div className="nav_list_item">
              <li>
                <button onClick={() => goToPage('trening', navigate)}>Trening</button>
              </li>
            </div>
            <div className="nav_list_item">
              <li>
                <button onClick={() => goToPage('forecast', navigate)}>Forecast action</button>
              </li>
            </div>
            <div className="nav_list_item">
              <li>
                <button onClick={() => goToPage('displayResults', navigate)}>
                  Display results
                </button>
              </li>
            </div>
          </ul>
        </div>
      </div>
    </div>
  );
}
