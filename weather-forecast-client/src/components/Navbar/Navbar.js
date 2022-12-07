import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../../css/Navbar.css';
import { goToPage } from '../../Helpers/RoutingHelper';
import iconImg from '../../images/snow.png';

export function Navbar(props) {
  const { pageName } = props;
  const navigate = useNavigate();
  return (
    <>
      <header id="navbar-wrapper">
        <nav id="navbar">
          <div className="navbar left">
            <img className="icon-img" src={iconImg} />
            <span className="gradient skew">
              <h1 className="logo un-skew">
                <span>{pageName}</span>
              </h1>
            </span>
            <button id="menu" className="btn-navbar">
              <span className="fas fa-bars"></span>
            </button>
          </div>
          <div className="navbar right">
            <button
              onClick={() => goToPage('/', navigate, { replace: true })}
              className="navbar-link">
              <span className="navbar-link-span">
                <span className="u-navbar">Home</span>
              </span>
            </button>
            <button
              onClick={() => goToPage('/importData', navigate, { replace: true })}
              className="navbar-link">
              <span className="navbar-link-span">
                <span className="u-navbar">Import Data</span>
              </span>
            </button>
            <button
              onClick={() => goToPage('/trening', navigate, { replace: true })}
              className="navbar-link">
              <span className="navbar-link-span">
                <span className="u-navbar">Trening</span>
              </span>
            </button>
            <button
              onClick={() => goToPage('/forecast', navigate, { replace: true })}
              className="navbar-link">
              <span className="navbar-link-span">
                <span className="u-navbar">Forecast</span>
              </span>
            </button>
            <button
              onClick={() => goToPage('/displayResults', navigate, { replace: true })}
              className="navbar-link">
              <span className="navbar-link-span">
                <span className="u-navbar">Display results</span>
              </span>
            </button>
          </div>
        </nav>
      </header>
      <main>
        <section id="home"></section>
        <section id="about"></section>
        <section id="work"></section>
        <section id="contact"></section>
      </main>
    </>
  );
}
