import React from 'react';

export function Loader(props) {
  const { loader } = props;
  return (
    <>
      {loader == true ? (
        <div className="loader">
          <div style={{ color: 'white' }}>IMPORTING DATA FROM CSV ...</div>
        </div>
      ) : null}
    </>
  );
}
