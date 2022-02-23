import React, { lazy, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import {
  Header, Icon, Label, Segment,
} from 'semantic-ui-react';
import 'moment/locale/fr';

const Moment = lazy(() => import('react-moment'));

const RequestMessagesFeed = lazy(() => import('@gesasso/components/RequestMessagesFeed'));

const StatusLabel = lazy(() => import('@gesasso/components/StatusLabel'));
const OriginIcon = lazy(() => import('@gesasso/components/OriginIcon'));
const LoaderOverlay = lazy(() => import('@gesasso/components/LoaderOverlay'));

const RequestView = () => {
  const { id } = useParams();
  const [request, setRequest] = useState(null);
  const [loading, setLoading] = useState(true);

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
    return <LoaderOverlay content="Fetching request ..." />;
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
