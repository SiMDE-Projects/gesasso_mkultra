import React from 'react';
import { Checkbox, Form, Segment } from 'semantic-ui-react';
import csrfToken from '@gesasso/utils/csrfToken';
import PropTypes from 'prop-types';

const RequestMessagesForm = ({ request, onSubmit }) => {
  const [isPrivate, setPrivate] = React.useState(false);
  const [busy, setBusy] = React.useState(false);
  const [message, setMessage] = React.useState('');

  const handleSubmit = (e) => {
    setBusy(true);
    e.preventDefault();
    fetch(`${process.env.GESASSO_BASE_URL}api/request_messages/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken(),
      },
      body: JSON.stringify({
        message,
        request: request.url,
        type: isPrivate ? 'INTERNAL' : 'PUBLIC',
        origin: 'WEB',
      }),
    }).then((response) => {
      if (response.status === 201) {
        response.json().then((validResponse) => {
          setMessage('');
          setBusy(false);
          onSubmit(validResponse);
        });
      } else {
        setBusy(false);
      }
    });
  };

  return (
    <Segment>
      <Form>
        <Form.TextArea
          name="message"
          placeholder="Votre message"
          rows={3}
          onChange={(e) => setMessage(e.target.value)}
          value={message}
        />
        <Form.Field>
          <Checkbox
            toggle
            label="Ce message contient des données privées"
            onChange={(e, data) => setPrivate(data.checked)}
            checked={isPrivate}
          />
        </Form.Field>
        <Form.Button
          content="Envoyer"
          labelPosition="left"
          icon="edit"
          primary
          disabled={busy}
          onClick={(e) => handleSubmit(e)}
        />
      </Form>
    </Segment>
  );
};

RequestMessagesForm.propTypes = {
  request: PropTypes.shape({
    id: PropTypes.number.isRequired,
    url: PropTypes.string.isRequired,
  }).isRequired,
  onSubmit: PropTypes.func,
};

RequestMessagesForm.defaultProps = {
  onSubmit: () => {
  },
};

export default RequestMessagesForm;
