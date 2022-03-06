import React, { useState } from 'react';
import {
  Button, Form, Input, Segment, TextArea,
} from 'semantic-ui-react';
import AssoSelector from '@gesasso/components/AssoSelector';
import csrfToken from '@gesasso/utils/csrfToken';
import DatePicker, { registerLocale } from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import fr from 'date-fns/locale/fr';

registerLocale('es', fr);

const RequestForm = () => {
  const [dueDate, setDueDate] = useState(null);
  const [asso, setAsso] = useState(null);
  const [title, setTitle] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    fetch('/api/requests/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken(),
      },
      body: JSON.stringify({
        asso,
        title,
        status: 'OPEN',
        origin: 'WEB',
        actions: [],
        due_date: dueDate,
        message,
      }),
    }).then((response) => {
      if (response.status === 201) {
        response.json().then((validResponse) => {
          window.location.href = `/requests/${validResponse.id}/`;
        });
      }
    });
  };

  return (
    <Segment>
      <Form>
        <Form.Field>
          <label>
            Asso
          </label>
          <AssoSelector
            onChange={(a) => {
              setAsso(a);
            }}
          />
        </Form.Field>
        <Form.Field>
          <label>Title</label>
          <Input placeholder="First Name" onChange={(e) => setTitle(e.target.value)} />
        </Form.Field>
        <Form.Field>
          <label>Description</label>
          <TextArea placeholder="Tell us more" onChange={(e) => setMessage(e.target.value)} />
        </Form.Field>
        <Form.Field>
          <label>Due date</label>
          <DatePicker selected={dueDate} onChange={(date: Date) => setDueDate(date)} />
        </Form.Field>
        <Button type="submit" onClick={(e) => handleSubmit(e)}>Submit</Button>
      </Form>
    </Segment>
  );
};

export default RequestForm;
