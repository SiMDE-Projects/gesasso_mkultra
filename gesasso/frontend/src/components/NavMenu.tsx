import React, { lazy } from 'react';
import { Menu } from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';

const UserInfo = lazy(() => import('@gesasso/components/UserInfo'));

const NavMenu = () => {
  const [activeItem, setActiveItem] = React.useState('Home');
  const navigate = useNavigate();
  const handleItemClick = (e, { name, url }) => {
    setActiveItem(name);
    navigate(url);
  };
  return (
    <Menu>
      <Menu.Item
        name="Home"
        url="/"
        active={activeItem === 'Home'}
        onClick={handleItemClick}
      />
      <Menu.Item
        name="New Request"
        url="/requests/new"
        active={activeItem === 'New Request'}
        onClick={handleItemClick}
      />
      <Menu.Menu position="right">
        <UserInfo />
      </Menu.Menu>
    </Menu>
  );
};

export default NavMenu;
