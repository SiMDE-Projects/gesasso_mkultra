import React, { useEffect, useState } from 'react';
import Moment from 'react-moment';
import 'moment/locale/fr';
import {
  Button, Dimmer, Icon, Image, Label, Loader, Popup, Segment, Table,
} from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';

Moment.globalLocale = 'fr';
Moment.globalLocal = true;

const RequestList = function () {
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
    return (
      <Segment>
        <Dimmer active>
          <Loader indeterminate>Fetching requests</Loader>
        </Dimmer>

        <Image src="https://react.semantic-ui.com/images/wireframe/short-paragraph.png" />
      </Segment>
    );
  }

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
    return <Label ribbon color="blue">Unknown</Label>;
  };

  const renderOrigin = (origin) => {
    switch (origin) {
      case 'WEB':
        return <Popup content="Web" position="right center" trigger={<Icon name="globe" />} />;
      case 'MAIL':
        return <Popup content="Mail" position="right center" trigger={<Icon name="mail" />} />;
      case 'DIRECT':
        return <Popup content="Direct" position="right center" trigger={<Icon name="phone" />} />;
      case 'MERGE':
        return <Popup content="Merged requests" position="right center" trigger={<Icon name="users" />} />;
      default:
        return <Popup content="Unknown" position="right center" trigger={<Icon name="question" />} />;
    }
  };

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
              {renderStatus(x.status)}
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
              {renderOrigin(x.origin)}
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
