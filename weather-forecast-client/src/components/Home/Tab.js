import React from 'react';
import { useNavigate } from 'react-router-dom';
import { goToPage } from '../../Helpers/RoutingHelper';

export function Tab(props) {
  const { url, tabText } = props;
  const navigate = useNavigate();

  return (
    <button className="navbar-link" onClick={() => goToPage(url, navigate, { replace: true })}>
      <span className="navbar-link-span">
        <span className="u-navbar">{tabText}</span>
      </span>
    </button>
  );
}
