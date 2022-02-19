import React from 'react';
import PropTypes from 'prop-types';

import { Icon, Popup } from 'semantic-ui-react';

function OriginIcon({ origin }) {
  let icon = 'question';
  let text = 'Type inconnu';
  switch (origin) {
    case 'WEB':
      icon = 'globe';
      text = 'Web';
      break;
    case 'MAIL':
      icon = 'mail';
      text = 'Mail';
      break;
    case 'DIRECT':
      icon = 'phone';
      text = 'Direct';
      break;
    default:
      break;
  }
  return <Popup content={text} position="right center" trigger={<Icon name={icon} />} />;
}

OriginIcon.propTypes = {
  origin: PropTypes.string.isRequired,
};

export default OriginIcon;
