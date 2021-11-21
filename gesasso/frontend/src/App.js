import React from 'react'
import { Container, Divider, Grid, Header, Icon,  Button, Checkbox, Form,TextArea,Select  } from 'semantic-ui-react'
import axios from 'axios'

const App = () => {
const countryOptions = [
      { key: '1', text: '1', value: '1' },
      { key: '2', text: '2', value: '2' },
      { key: '3', text: '3', value: '3' },
      { key: '4', text: '4', value: '4' },
      { key: '5', text: '5', value: '5' },
      { key: '6', text: '6', value: '6' },
      { key: '7', text: '7', value: '7' },
      { key: '8', text: '8', value: '8' },
      { key: '9', text: '9', value: '9' },
      { key: '10', text: '10', value: '10' },
    ];
    React.useEffect(() => {
      axios.get('/api/me/')
      .then(res => {
        console.log(res.data)
      })
    }, [])

return (
  <Container>
    <style>
      {`
      html, body {
        background-color: #252839 !important;
      }
      p {
        align-content: center;
        background-color: #495285;
        color: #fff;
        display: flex;
        flex-direction: column;
        justify-content: center;
        min-height: 6em;
      }
      p > span {
        opacity: 0.4;
        text-align: center;
      }
    }
    `}
    </style>

    <Header as='h2' icon inverted textAlign='center'>
      <Icon name='grid layout' />
      Ges'Asso
      <Header.Subheader>
        Gestion des demandes SiMDE & Pay'UTC
      </Header.Subheader>
    </Header>
    <Divider />

    <Header as='h2' inverted textAlign='center'>
      Basic 16
    </Header>
    <Grid>
      <Grid.Row>
        <Grid.Column>
          <p align="center">
          <Form>

    <Form.Field>
      <label>Titre de la demande</label>
      <input placeholder='Titre' />
    </Form.Field>
    <Form.Field>
      <label>Contenu</label>
      <TextArea placeholder='First Name' />
    </Form.Field>
    <Form.Field>
    <Select placeholder='Select your country' options={countryOptions} />
    </Form.Field>
    <Button type='submit'>Submit</Button>
  </Form>
          </p>

        </Grid.Column>
      </Grid.Row>
    </Grid>
  </Container>)
}

export default App
