import React from 'react';
import PropTypes from 'prop-types';
import {
  Dimmer, Image, Loader, Segment,
} from 'semantic-ui-react';

export interface Props {
  content: React.ReactNode,
}

const LoaderOverlay = ({ content }: Props) => (
  <Segment>
    <Dimmer active>
      <Loader indeterminate>{content}</Loader>
    </Dimmer>
    <Image src="https://react.semantic-ui.com/images/wireframe/short-paragraph.png" />
  </Segment>
);

LoaderOverlay.defaultProps = {
  content: 'Loading...',
};

LoaderOverlay.propTypes = {
  content: PropTypes.string,
};

export default LoaderOverlay;
