import React, { useContext } from 'react';
import RequestList from './RequestList';
import SessionContext from './SessionContext';

const HomePage = function () {
  const context = useContext(SessionContext);

  return context.user !== null && <RequestList />;
};

export default HomePage;
