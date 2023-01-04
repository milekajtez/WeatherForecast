import React from 'react';

export function Loader(props) {
  const { loader, text } = props;
  return (
    <>
      {loader == true ? (
        <div className="loader">
          <div style={{ color: 'white' }}>{text}</div>
        </div>
      ) : null}
    </>
  );
}
