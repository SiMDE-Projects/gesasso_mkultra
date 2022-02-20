import React, { lazy, useContext } from 'react';
import SessionContext from '@gesasso/SessionContext';

const RequestList = lazy(() => import('@gesasso/RequestList'));

const HomePage = () => {
  const context = useContext(SessionContext);

  return context.user !== null && <RequestList />;
};

export default HomePage;
