import React, { lazy } from 'react';
import { Container, Header, Menu } from 'semantic-ui-react';
import { Outlet } from 'react-router-dom';

const UserInfo = lazy(() => import('@gesasso/components/UserInfo'));

const Layout = () => {
  const [activeItem, setActiveItem] = React.useState('Home');
  const handleItemClick = (e, { name }) => setActiveItem(name);
  return (
    <Container>
      <Header textAlign="center">
        <Menu>
          <Menu.Item
            name="Home"
            active={activeItem === 'Home'}
            onClick={handleItemClick}
          />
          <Menu.Item
            name="New Request"
            active={activeItem === 'New Request'}
            onClick={handleItemClick}
          />
          <Menu.Menu position="right">
            <UserInfo />
          </Menu.Menu>
        </Menu>
      </Header>
      <Outlet />
    </Container>
  );
};

export default Layout;
