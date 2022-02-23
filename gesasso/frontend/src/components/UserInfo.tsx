import React, { useContext, useEffect, useState } from 'react';
import { Button, Menu } from 'semantic-ui-react';

import SessionContext from '@gesasso/utils/SessionContext';

const UserInfo = () => {
  const [loading, setLoading] = useState(true);
  const [authLink, setAuthLink] = useState('');
  const context = useContext(SessionContext);
  const authlinkUrl = '/oauth/authlink';
  const userInfosUrl = '/proxy_pda/get_user_infos';

  useEffect(() => {
    fetch(userInfosUrl)
      .then((response) => {
        if (response.status === 200) {
          response.json().then((validResponse) => {
            context.updateUser(validResponse);
            setLoading(false);
          });
        } else {
          fetch(authlinkUrl)
            .then((response2) => response2.json())
            .then((response2) => {
              setAuthLink(response2.link);
              setLoading(false);
            });
        }
      });
  }, []);

  if (loading) {
    return <Menu.Item>Loading...</Menu.Item>;
  }

  if (context.user !== null) {
    return (
      <>
        <Menu.Item>
          {context.user.firstname}
          {' '}
          {context.user.lastname}
        </Menu.Item>
        <Menu.Item>
          <Button onClick={() => {
            window.location.href = '/oauth/logout';
          }}
          >
            Déconnexion
          </Button>
        </Menu.Item>
      </>
    );
  }

  return (
    <Menu.Item>
      <Button onClick={() => {
        window.location.href = authLink;
      }}
      >
        Connexion
      </Button>
    </Menu.Item>
  );
};

export default UserInfo;
