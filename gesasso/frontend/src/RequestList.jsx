import React, { useEffect, useState } from 'react';
import Moment from 'react-moment';
import 'moment/locale/fr';
import {
  Dimmer, Image, Label, Loader, Segment, Table,
} from 'semantic-ui-react';
import AssoSelector from '@gesasso/components/AssoSelector';

Moment.globalLocale = 'fr';
Moment.globalLocal = true;

const RequestList = function () {
  const [loading, setLoading] = useState(true);
  const [requests, setRequests] = useState([]);
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

  const translateStatus = (status) => {
    switch (status) {
      case 1:
        return <Label ribbon color="yellow">Pending</Label>;
      case 2:
        return <Label ribbon color="green">Approved</Label>;
      case 3:
        return <Label ribbon color="red">Rejected</Label>;
      default:
        return <Label ribbon color="blue">Unknown</Label>;
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
        </Table.Row>
      </Table.Header>
      <Table.Body>
        {requests.map((x) => (
          <Table.Row key={x.id}>
            <Table.Cell>
              {translateStatus(x.status)}
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
              {x.origin}
            </Table.Cell>
            <Table.Cell>
              {x.messages.length}
            </Table.Cell>
            <Table.Cell>
              <Moment locale="fr" format="LLLL">{x.due_date}</Moment>
              <Label>
                <Moment to={x.due_date} />
                <AssoSelector />
              </Label>
            </Table.Cell>
          </Table.Row>
        ))}
      </Table.Body>
    </Table>
  );
};

export default RequestList;
