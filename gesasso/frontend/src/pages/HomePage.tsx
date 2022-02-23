import React, { lazy, useContext } from 'react';
import SessionContext from '@gesasso/utils/SessionContext';

const RequestList = lazy(() => import('@gesasso/pages/RequestList'));

const HomePage = () => {
  const context = useContext(SessionContext);

  return context.user !== null && <RequestList />;
};

export default HomePage;
