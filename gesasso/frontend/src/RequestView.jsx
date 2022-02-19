import React, { useEffect } from 'react';
import { useParams } from 'react-router-dom';
import Moment from 'react-moment';
import 'moment/locale/fr';
import {
  Dimmer, Header, Icon, Image, Label, Loader, Segment,
} from 'semantic-ui-react';
import StatusLabel from '@gesasso/components/StatusLabel';
import OriginIcon from '@gesasso/components/OriginIcon';
import RequestMessagesFeed from '@gesasso/components/RequestMessagesFeed';

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
        <StatusLabel status={request.status} />
        {request.title}
        <Header.Subheader>
          <OriginIcon origin={request.origin} />
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
      <RequestMessagesFeed messages={request.messages} />
    </Segment>
  );
};

export default RequestView;
