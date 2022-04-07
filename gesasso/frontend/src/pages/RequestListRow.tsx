import React from 'react';
import {
  Button, Icon, Label, Table,
} from 'semantic-ui-react';
import { useNavigate } from 'react-router-dom';
import 'moment/locale/fr';
import PropTypes from 'prop-types';

const Moment = React.lazy(() => import('react-moment'));

const StatusLabel = React.lazy(() => import('@gesasso/components/StatusLabel'));
const OriginIcon = React.lazy(() => import('@gesasso/components/OriginIcon'));

const RequestListRow = ({ request }) => {
  const navigate = useNavigate();

  return (
    <Table.Row key={request.id}>
      <Table.Cell>
        <StatusLabel status={request.status} />
      </Table.Cell>
      <Table.Cell>
        {request.title}
      </Table.Cell>
      <Table.Cell>
        {request.user ? request.user.full_name : request.custom_author_name}
      </Table.Cell>
      <Table.Cell>
        {request.asso ? request.asso.shortname : 'N/C'}
      </Table.Cell>
      <Table.Cell>
        <OriginIcon origin={request.origin} />
      </Table.Cell>
      <Table.Cell>
        {
                    request.due_date
                      ? (
                        <>
                          <Moment locale="fr" format="LLLL">{request.due_date}</Moment>
                          <Label>
                            <Moment to={request.due_date} />
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
            navigate(`/requests/${request.id}`);
          }}
        >
          <Icon name="eye" />
        </Button>
      </Table.Cell>
    </Table.Row>
  );
};

RequestListRow.propTypes = {
  request: PropTypes.shape({
    id: PropTypes.number.isRequired,
    status: PropTypes.string.isRequired,
    title: PropTypes.string.isRequired,

    asso: PropTypes.shape({
      shortname: PropTypes.string.isRequired,
    }).isRequired,
    user: PropTypes.shape({
      full_name: PropTypes.string.isRequired,
    }).isRequired,
    custom_author_name: PropTypes.string,
    message: PropTypes.shape({
      type: PropTypes.string.isRequired,
      id: PropTypes.number.isRequired,
      user: PropTypes.shape({
        full_name: PropTypes.string.isRequired,
      }).isRequired,
      message: PropTypes.string.isRequired,
      created: PropTypes.string.isRequired,
    }).isRequired,
    origin: PropTypes.string.isRequired,
    due_date: PropTypes.string.isRequired,
  }).isRequired,
};

export default RequestListRow;
