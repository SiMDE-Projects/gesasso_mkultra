import React from 'react';

export interface ContextState {
  user: { firstname: string, lastname: string } | null;
  updateUser: (data: object) => void;
}

const SessionContext = React.createContext({
  user: null,
  updateUser: (data) => {
    // eslint-disable-next-line no-console
    console.error('updateUser not implemented', data);
  },
} as ContextState);

export default SessionContext;
