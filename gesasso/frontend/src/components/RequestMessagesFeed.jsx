import React from 'react';
import PropTypes from 'prop-types';
import Moment from 'react-moment';
import 'moment/locale/fr';
import { Feed, Header, Label } from 'semantic-ui-react';

function RequestMessagesFeed({ messages }) {
  return (
    <Feed>
      <Header as="h3" dividing>
        Messages
      </Header>
      {messages && messages.map((message) => (
        <Feed.Event key={message.id}>
          <Feed.Label icon="pencil" />
          <Feed.Content>
            <Feed.Summary>
              <Feed.User>{message.user.full_name}</Feed.User>
              <Feed.Date>
                <Moment locale="fr" format="LLLL">{message.created}</Moment>
                <Label>
                  <Moment to={message.created} />
                </Label>
              </Feed.Date>
            </Feed.Summary>
            <Feed.Extra text>{message.message}</Feed.Extra>
          </Feed.Content>
        </Feed.Event>
      ))}
    </Feed>
  );
}

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
