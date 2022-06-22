import React from 'react';
import ReactDOM from 'react-dom';
import * as Sentry from '@sentry/react';
import { BrowserTracing } from '@sentry/tracing';
import App from '@gesasso/App';
import 'semantic-ui-css/semantic.min.css';

Sentry.init({
  dsn: 'https://0741301057b7434c82d55b66b58e5799@o1296214.ingest.sentry.io/6522752',
  integrations: [new BrowserTracing()],
  tracesSampleRate: 1.0,
});

ReactDOM.render(
  <App />,
  document.getElementById('app'),
);
