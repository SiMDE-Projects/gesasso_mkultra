import React from 'react';
import { Link } from 'react-router-dom';

const NotFound = function () {
  return (
    <div>
      <h1>Page not found</h1>
      <p>
        <Link to="/">Go to the home page</Link>
      </p>
    </div>
  );
};

export default NotFound;
