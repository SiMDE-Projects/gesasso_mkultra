// noinspection JSCheckFunctionSignatures

import React, { lazy, Suspense } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Dimmer, Loader } from 'semantic-ui-react';
import RequestView from '@gesasso/RequestView';
import SessionContext from '@gesasso/SessionContext';

const HomePage = lazy(() => import('./HomePage'));
const Layout = lazy(() => import('./Layout'));
const NotFound = lazy(() => import('./NotFound'));

const App = function () {
  const [user, setUser] = React.useState(null);
  const updateUser = function (datas) {
    setUser(datas);
  };

  return (
    <>
      <style>
        {`
      html, body {
        background-color: #252839 !important;
      }
      p {
        align-content: center;
        background-color: #495285;
        color: white;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 6em;
      }
    `}
      </style>
      <Suspense fallback={(
        <Dimmer active>
          <Loader indeterminate>Loading Ges'Asso</Loader>
        </Dimmer>
      )}
      >
        <SessionContext.Provider value={{ user, updateUser }}>
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<Layout />}>
                <Route path="/" element={<HomePage />} />
                <Route path="/requests/:id" element={<RequestView />} />
                <Route path="*" element={<NotFound />} />
              </Route>
            </Routes>
          </BrowserRouter>
        </SessionContext.Provider>
      </Suspense>
    </>
  );
};

export default App;
