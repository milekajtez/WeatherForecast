import React from 'react';
import '../../css/Navbar.css';
import { tabs } from '../../Helpers/TabHelper';
import { Tab } from '../Home/Tab';
import { Logo } from './Logo';
import { Routing } from './Routing';

export function Navbar() {
  return (
    <>
      <header id="navbar-wrapper" className="hover-underline-animation">
        <nav id="navbar">
          <Logo />
          <div className="navbar right">
            {tabs.map((item, index) => {
              return <Tab key={index} url={item.url} tabText={item.tabName} />;
            })}
          </div>
        </nav>
      </header>
      <Routing />
    </>
  );
}
