import React from 'react';

import { Dimmer, Loader } from 'semantic-ui-react';

const Fallback = () => (
  <Dimmer active>
    <Loader indeterminate>Loading Ges&lsquo;Asso</Loader>
  </Dimmer>
);

export default Fallback;
