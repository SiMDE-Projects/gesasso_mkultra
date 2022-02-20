// noinspection JSCheckFunctionSignatures

import React, { lazy, Suspense, useState } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Fallback from '@gesasso/components/Fallback';
import SessionContext from '@gesasso/SessionContext';

const RequestView = lazy(() => import('@gesasso/RequestView'));
const HomePage = lazy(() => import('@gesasso/HomePage'));
const Layout = lazy(() => import('@gesasso/Layout'));
const NotFound = lazy(() => import('@gesasso/NotFound'));

const App = () => {
  const [user, setUser] = useState(null);
  const updateUser = (datas) => {
    setUser(datas);
  };

  return (
    <>
      <style>
        {`
      html, body {
        background-color: #252839 !important;
      }
    `}
      </style>
      <Suspense fallback={<Fallback />}>
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
