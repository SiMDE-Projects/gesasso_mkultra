import React, { useEffect, useState } from 'react';
import { Label, Table } from 'semantic-ui-react';

const RequestList = function () {
  const [loading, setLoading] = useState(true);
  const [requests, setRequests] = useState([]);
  useEffect(() => {
    fetch('/api/requests/')
      .then((response) => response.json())
      .then((data) => {
        setRequests(data.results);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading...</p>;
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
    <>
      <p>Mes demandes</p>
      <Table>
        <Table.Header>
          <Table.Row>
            <Table.HeaderCell>Status</Table.HeaderCell>
            <Table.HeaderCell>Title</Table.HeaderCell>
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
                {x.due_date}
              </Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table>
    </>
  );
};

export default RequestList;
