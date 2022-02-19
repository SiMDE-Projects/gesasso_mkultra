import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Moment from 'react-moment';
import 'moment/locale/fr';
import {
  Dimmer, Feed, Header, Icon, Image, Label, Loader, Popup, Segment,
} from 'semantic-ui-react';

const RequestView = function () {
  const { id } = useParams();
  const [request, setRequest] = React.useState(null);
  const [loading, setLoading] = React.useState(true);

  useEffect(() => {
    fetch(`/api/requests/${id}/`)
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        }
        return new Promise((resolve) => {
          resolve({ results: [] });
        });
      })
      .then((data) => {
        setRequest(data);
        setLoading(false);
      });
  }, []);

  const renderOrigin = (origin) => {
    let icon = '';
    let text = '';
    switch (origin) {
      case 'WEB':
        icon = 'globe';
        text = 'Web';
        break;
      case 'MAIL':
        icon = 'mail';
        text = 'Mail';
        break;
      case 'DIRECT':
        icon = 'phone';
        text = 'Direct';
        break;
      default:
        icon = 'question';
        text = 'Type inconnu';
        break;
    }
    return <Popup content={text} position="right center" trigger={<Icon name={icon} />} />;
  };

  const renderStatus = (status) => {
    let color = '';
    let text = '';
    switch (status) {
      case 'OPEN':
        color = 'purple';
        text = 'Pending';
        break;
      case 'ASSIGNED':
        color = 'yellow';
        text = 'Assigned to tech';
        break;
      case 'CLOSED':
        color = 'red';
        text = 'Closed';
        break;
      case 'DONE':
        color = 'green';
        text = 'Done';
        break;
      case 'WAITING_TECH':
        color = 'orange';
        text = 'Waiting for tech';
        break;
      case 'WAITING_FOR_TIERS_SERVICE':
        color = 'orange';
        text = 'Waiting for tiers service';
        break;
      case 'WAITING_FOR_CUSTOMER':
        color = 'orange';
        text = 'Waiting for customer';
        break;
      default:
        color = 'blue';
        text = 'Unknown';
        break;
    }
    return <Label ribbon color={color}>{text}</Label>;
  };

  if (loading) {
    return (
      <Segment>
        <Dimmer active>
          <Loader indeterminate>Fetching request</Loader>
        </Dimmer>
        <Image src="https://react.semantic-ui.com/images/wireframe/short-paragraph.png" />
      </Segment>
    );
  }

  return (
    <Segment style={{ background: 'white' }}>
      <Header as="h1">
        {renderStatus(request.status)}
        {request.title}
        <Header.Subheader>
          {renderOrigin(request.origin)}
          <Moment locale="fr" format="LLLL">{request.created}</Moment>
          <Label>
            <Moment to={request.created} />
          </Label>
        </Header.Subheader>
        <Header.Subheader>
          <Icon name="building" />
          {request.asso.shortname}
        </Header.Subheader>
        <Header.Subheader>
          <Icon name="user" />
          {request.user.full_name}
        </Header.Subheader>
      </Header>
      <Feed>
        <Header as="h3" dividing>
          Messages
        </Header>
        {request.messages && request.messages.map((message) => (
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
    </Segment>
  );
};

export default RequestView;
