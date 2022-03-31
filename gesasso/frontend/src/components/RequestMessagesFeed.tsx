import React from 'react';
import PropTypes from 'prop-types';
import { Feed, Header } from 'semantic-ui-react';
import 'moment/locale/fr';
import FeedMessage from '@gesasso/components/FeedMessage';

const RequestMessagesFeed = ({ messages }) => (
  <Feed>
    <Header as="h3" dividing>
      Messages
    </Header>
    {messages && messages.map((message) => (
      <FeedMessage
        key={message.id}
        message={message}
      />
    ))}
  </Feed>
);

RequestMessagesFeed.propTypes = {
  messages: PropTypes.arrayOf(PropTypes.shape({
    id: PropTypes.number.isRequired,
    user: PropTypes.shape({
      full_name: PropTypes.string.isRequired,
    }).isRequired,
    message: PropTypes.string.isRequired,
    created: PropTypes.string.isRequired,
  })).isRequired,
};

export default RequestMessagesFeed;
