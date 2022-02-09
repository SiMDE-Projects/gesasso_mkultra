import React, {useEffect, useState} from 'react';

const UserInfo = () => {
  const [userName, setUserName] = useState('');
  const [loading, setLoading] = useState(true);
  const [authLink, setAuthLink] = useState('');
  const authlinkUrl = '/oauth/authlink';
  const logoutUrl = '/oauth/logout';
  const userInfosUrl = '/proxy_pda/get_user_infos';

  // récupération du lien de connexion depuis le backend de Flairsou
  useEffect(() => {
    fetch(authlinkUrl)
      .then((response) => response.json())
      .then((response) => {
        setAuthLink(response.link);
      });
  }, []);

  // vérification si l'utilisateur est déjà connecté, uniquement au
  // chargement du composant
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
    // the user is connected, return a component with the name
    // of the user
    return (
      <p>
        {userName}
        <a href={logoutUrl}>Déconnexion</a>
      </p>
    );
  }

  // the user is not connected, display the login link

  return (
    <p>
      <a href={authLink}>Connexion</a>
    </p>
  );
};

export default UserInfo;
