import React, { lazy, Suspense } from 'react';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
// import Layout from './Layout';
// import HomePage from './HomePage';

const HomePage = lazy(() => import('./HomePage'));
const Layout = lazy(() => import('./Layout'));
const NotFound = lazy(() => import('./NotFound'));

const App = function () {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<HomePage />} />
            <Route path="*" element={<NotFound />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </Suspense>
  );
};

export default App;
