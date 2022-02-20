import React from 'react';

const SessionContext = React.createContext({
  user: null,
  updateUser: () => {
    // eslint-disable-next-line no-console
    console.error('updateUser not implemented');
  },
});

export default SessionContext;
