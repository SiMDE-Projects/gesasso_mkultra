import React, { Suspense } from 'react';
import { Container, Header } from 'semantic-ui-react';
import { Outlet } from 'react-router-dom';
import NavMenu from '@gesasso/components/NavMenu';
import LoaderOverlay from '@gesasso/components/LoaderOverlay';

const Layout = () => (
  <Container>
    <Header textAlign="center">
      <NavMenu />
    </Header>
    <Suspense fallback={<LoaderOverlay />}>
      <Outlet />
    </Suspense>
  </Container>
);

export default Layout;
