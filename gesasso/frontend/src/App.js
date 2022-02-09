import React from 'react';
import {Container, Header} from 'semantic-ui-react';
import UserInfo from './UserInfo';

const App = function () {
  const assoListLink = '/proxy_pda/get_list_assos';
  const [assosFetched, setAssosFetched] = React.useState('');

  return (
    <Container>
      <style>
        {`
      html, body {
        background-color: #252839 !important;
      }
      p {
        align-content: center;
        background-color: #495285;
        color: #fff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 6em;
      }
      p > span {
        opacity: 0.4;
        text-align: center;
      }
    }
    `}
      </style>

      <Header as="h2" icon inverted textAlign="center">
        <UserInfo/>
      </Header>
    </Container>
  );
};

export default App;
