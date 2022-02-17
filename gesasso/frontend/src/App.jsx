// noinspection JSCheckFunctionSignatures

import React, { lazy, Suspense } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import { Container, Header } from 'semantic-ui-react';
import SessionContext from './SessionContext';
import AssoSelector from '@gesasso/components/AssoSelector';

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
        <Container>
          <Header as="h2" icon inverted textAlign="center">
            Loading ...
          </Header>
        </Container>
      )}
      >
        <SessionContext.Provider value={{ user, updateUser }}>
          <BrowserRouter>
            <Routes>
              <Route path="/" element={<Layout />}>
                <Route path="/" element={<HomePage />} />
                <Route path="/req" element={<AssoSelector />} />
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
