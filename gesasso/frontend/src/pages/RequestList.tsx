import React, { Suspense, useEffect, useState } from 'react';
import { Table } from 'semantic-ui-react';
import 'moment/locale/fr';

const RequestListRow = React.lazy(() => import('@gesasso/pages/RequestListRow'));
const LoaderOverlay = React.lazy(() => import('@gesasso/components/LoaderOverlay'));

const RequestList = () => {
  const [loading, setLoading] = useState(true);
  const [requests, setRequests] = useState([]);

  useEffect(() => {
    fetch(`${process.env.GESASSO_BASE_URL}api/requests/`)
      .then((response) => {
        if (response.status === 200) {
          return response.json();
        }
        return new Promise((resolve) => {
          resolve([]);
        });
      })
      .then((data) => {
        setRequests(data);
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
          <Table.HeaderCell>Due date</Table.HeaderCell>
          <Table.HeaderCell>Actions</Table.HeaderCell>
        </Table.Row>
      </Table.Header>
      <Table.Body>
        <Suspense fallback={<Table.Row><LoaderOverlay /></Table.Row>}>
          {requests.map((x) => (
            <RequestListRow request={x} key={x.id} />
          ))}
        </Suspense>
      </Table.Body>
    </Table>
  );
};

export default RequestList;
