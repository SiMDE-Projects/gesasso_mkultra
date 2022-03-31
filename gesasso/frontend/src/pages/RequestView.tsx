import React, {
  lazy, Suspense, useEffect, useState,
} from 'react';
import { useParams } from 'react-router-dom';
import {
  Header, Icon, Label, Segment,
} from 'semantic-ui-react';
import 'moment/locale/fr';

const RequestMessageForm = lazy(() => import('@gesasso/components/RequestMessageForm'));
const NotFound = lazy(() => import('@gesasso/pages/NotFound'));
const Moment = lazy(() => import('react-moment'));
const RequestMessagesFeed = lazy(() => import('@gesasso/components/RequestMessagesFeed'));
const StatusLabel = lazy(() => import('@gesasso/components/StatusLabel'));
const OriginIcon = lazy(() => import('@gesasso/components/OriginIcon'));
const LoaderOverlay = lazy(() => import('@gesasso/components/LoaderOverlay'));

const RequestView = () => {
  const { id } = useParams();
  const [request, setRequest] = useState(null);
  const [messages, setMessages] = useState(null);
  const [loading, setLoading] = useState(true);
  const [messagesLoading, setMessagesLoading] = useState(true);

  const fetchRequest = () => fetch(`${process.env.BASE_URL}/api/requests/${id}/`)
    .then((response) => {
      if (response.status === 200) {
        return response.json();
      }
      return new Promise((resolve) => {
        resolve(null);
      });
    })
    .then((data) => {
      setRequest(data);
      setLoading(false);
    });

  const fetchMessages = () => fetch(`${process.env.BASE_URL}/api/request_messages/?request=${id}`)
    .then((response) => {
      if (response.status === 200) {
        return response.json();
      }
      return new Promise((resolve) => {
        resolve([]);
      });
    })
    .then((data) => {
      setMessages(data);
      setMessagesLoading(false);
    });

  useEffect(() => {
    fetchRequest();
    fetchMessages();
  }, []);

  if (loading) {
    return <LoaderOverlay content="Fetching request ..." />;
  }

  if (!request) {
    return <NotFound />;
  }

  return (
    <Suspense fallback={<LoaderOverlay />}>
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
        {messagesLoading ? (
          <LoaderOverlay content="Loading messages ..." />
        ) : (
          <RequestMessagesFeed messages={messages} />
        )}
        <RequestMessageForm
          request={request}
          onSubmit={() => {
            fetchMessages();
          }}
        />
      </Segment>
    </Suspense>
  );
};

export default RequestView;
