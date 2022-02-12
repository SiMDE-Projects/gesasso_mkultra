import React from 'react';
import { Container, Header } from 'semantic-ui-react';
import UserInfo from './UserInfo';
import RequestList from './RequestList';

const HomePage = function () {
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
        <UserInfo />
        <RequestList />
      </Header>
    </Container>
  );
};

export default HomePage;
