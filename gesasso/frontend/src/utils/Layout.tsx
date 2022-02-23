import React from 'react';
import { Container, Header } from 'semantic-ui-react';
import { Outlet } from 'react-router-dom';
import NavMenu from '@gesasso/components/NavMenu';

const Layout = () => (
  <Container>
    <Header textAlign="center">
      <NavMenu />
    </Header>
    <Outlet />
  </Container>
);

export default Layout;
