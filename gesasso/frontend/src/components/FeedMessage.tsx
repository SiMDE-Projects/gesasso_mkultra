import React, { Suspense } from 'react';
import {
  Feed, Icon, Label, Message,
} from 'semantic-ui-react';
import 'moment/locale/fr';
import PropTypes from 'prop-types';

const Moment = React.lazy(() => import('react-moment'));
const LoaderOverlay = React.lazy(() => import('@gesasso/components/LoaderOverlay'));

const FeedMessage = ({ message }) => {
  const generateMessage = () => {
    let ret = null;
    switch (message.type) {
      case 'SUCCESS':
        ret = (
          <Message positive key={message.id}>
            <Message.Header>
              <Moment locale="fr" format="LLLL">{message.created}</Moment>
              <Label>
                <Moment to={message.created} />
              </Label>
            </Message.Header>
            {message.message}
          </Message>
        );
        break;
      case 'INFO':
        ret = (
          <Message info key={message.id}>
            <Message.Header>
              <Moment locale="fr" format="LLLL">{message.created}</Moment>
              <Label>
                <Moment to={message.created} />
              </Label>
            </Message.Header>
            {message.message}
          </Message>
        );
        break;
      case 'WARNING':
        ret = (
          <Message warning key={message.id}>
            <Message.Header>
              <Moment locale="fr" format="LLLL">{message.created}</Moment>
              <Label>
                <Moment to={message.created} />
              </Label>
            </Message.Header>
            {message.message}
          </Message>
        );
        break;
      case 'ERROR':
        ret = (
          <Message error key={message.id}>
            <Message.Header>
              <Moment locale="fr" format="LLLL">{message.created}</Moment>
              <Label>
                <Moment to={message.created} />
              </Label>
            </Message.Header>
            {message.message}
          </Message>
        );
        break;
      default:
        ret = (
          <Feed.Event key={message.id}>
            <Feed.Label icon="pencil" />
            <Feed.Content>
              <Feed.Summary>
                <Feed.User>
                  {message.type === 'INTERNAL' && <Icon name="lock" />}
                  {message.user.full_name}
                </Feed.User>
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
        );
        break;
    }
    return ret;
  };

  return (
    <Suspense fallback={<LoaderOverlay />}>
      {generateMessage()}
    </Suspense>
  );
};

FeedMessage.propTypes = {
  message: PropTypes.shape({
    id: PropTypes.number.isRequired,
    type: PropTypes.string.isRequired,
    user: PropTypes.shape({
      full_name: PropTypes.string.isRequired,
    }).isRequired,
    message: PropTypes.string.isRequired,
    created: PropTypes.string.isRequired,
  }).isRequired,
};

export default FeedMessage;
