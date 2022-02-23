import React from 'react';
import PropTypes from 'prop-types';

import { Icon, Popup, SemanticICONS } from 'semantic-ui-react';

export interface OriginIconProps {
  origin: 'WEB' | 'MAIL' | 'DIRECT';
}

const OriginIcon = ({ origin }: OriginIconProps) => {
  let icon: SemanticICONS = 'question';
  let text: string = 'Type inconnu';
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
};

OriginIcon.propTypes = {
  origin: PropTypes.string.isRequired,
};

export default OriginIcon;
