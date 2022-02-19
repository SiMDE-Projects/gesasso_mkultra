import React from 'react';
import PropTypes from 'prop-types';

import { Label } from 'semantic-ui-react';

function StatusLabel({ status }) {
  let color = 'blue';
  let text = 'Unknown';
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
      break;
  }
  return <Label ribbon color={color}>{text}</Label>;
}

StatusLabel.propTypes = {
  status: PropTypes.string.isRequired,
};

export default StatusLabel;
