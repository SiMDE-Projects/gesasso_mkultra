import React, { useEffect, useState } from 'react';
import {
  Button, Icon, Label, Table,
} from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';
import 'moment/locale/fr';

const Moment = React.lazy(() => import('react-moment'));

const StatusLabel = React.lazy(() => import('@gesasso/components/StatusLabel'));
const OriginIcon = React.lazy(() => import('@gesasso/components/OriginIcon'));

const LoaderOverlay = React.lazy(() => import('@gesasso/components/LoaderOverlay'));

const RequestList = () => {
  const [loading, setLoading] = useState(true);
  const [requests, setRequests] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetch('/api/requests/')
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        }
        return new Promise((resolve) => {
          resolve({ results: [] });
        });
      })
      .then((data) => {
        setRequests(data.results);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <LoaderOverlay content="Fetching requests ..." />;
  }

  return (
    <Table celled>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>Status</Table.HeaderCell>
          <Table.HeaderCell>Title</Table.HeaderCell>
          <Table.HeaderCell>Owner</Table.HeaderCell>
          <Table.HeaderCell>Asso</Table.HeaderCell>
          <Table.HeaderCell>Origin</Table.HeaderCell>
          <Table.HeaderCell>Messages</Table.HeaderCell>
          <Table.HeaderCell>Due date</Table.HeaderCell>
          <Table.HeaderCell>Actions</Table.HeaderCell>
        </Table.Row>
      </Table.Header>
      <Table.Body>
        {requests.map((x) => (
          <Table.Row key={x.id}>
            <Table.Cell>
              <StatusLabel status={x.status} />
            </Table.Cell>
            <Table.Cell>
              {x.title}
            </Table.Cell>
            <Table.Cell>
              {x.user.full_name}
            </Table.Cell>
            <Table.Cell>
              {x.asso.shortname}
            </Table.Cell>
            <Table.Cell>
              <OriginIcon origin={x.origin} />
            </Table.Cell>
            <Table.Cell>
              {x.messages.length}
            </Table.Cell>
            <Table.Cell>
              {
                                x.due_date
                                  ? (
                                    <>
                                      <Moment locale="fr" format="LLLL">{x.due_date}</Moment>
                                      <Label>
                                        <Moment to={x.due_date} />
                                      </Label>
                                    </>
                                  )
                                  : (
                                    <Label>
                                      No due date
                                    </Label>
                                  )
                            }
            </Table.Cell>
            <Table.Cell>
              <Button
                icon
                color="blue"
                onClick={() => {
                  navigate(`/requests/${x.id}`);
                }}
              >
                <Icon name="eye" />
              </Button>
            </Table.Cell>
          </Table.Row>
        ))}
      </Table.Body>
    </Table>
  );
};

export default RequestList;
