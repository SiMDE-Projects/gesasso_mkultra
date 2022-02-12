import React, { useEffect, useState } from 'react';

const UserInfo = function () {
  const [userName, setUserName] = useState('');
  const [loading, setLoading] = useState(true);
  const [authLink, setAuthLink] = useState('');
  const authlinkUrl = '/oauth/authlink';
  const logoutUrl = '/oauth/logout';
  const userInfosUrl = '/proxy_pda/get_user_infos';

  useEffect(() => {
    fetch(userInfosUrl)
      .then((response) => {
        if (response.status === 200) {
          response.json().then((validResponse) => {
            const fullName = `${validResponse.firstname} ${validResponse.lastname}`;
            setUserName(fullName);
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
    return <p>Loading...</p>;
  }

  if (userName !== '') {
    return (
      <p>
        {userName}
        <a href={logoutUrl}>Déconnexion</a>
      </p>
    );
  }

  return (
    <p>
      <a href={authLink}>Connexion</a>
    </p>
  );
};

export default UserInfo;
