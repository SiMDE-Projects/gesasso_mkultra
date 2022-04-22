import React, {lazy, useEffect, useState} from 'react';
import {useParams} from 'react-router-dom';
import {
    Header, Icon, Label, Segment, Grid
} from 'semantic-ui-react';
import 'moment/locale/fr';
import RequestMessageForm from '@gesasso/components/RequestMessageForm';
import RequestStatusSelector from '@gesasso/components/RequestStatusSelector';

const Moment = lazy(() => import('react-moment'));

const RequestMessagesFeed = lazy(() => import('@gesasso/components/RequestMessagesFeed'));

const StatusLabel = lazy(() => import('@gesasso/components/StatusLabel'));
const OriginIcon = lazy(() => import('@gesasso/components/OriginIcon'));
const LoaderOverlay = lazy(() => import('@gesasso/components/LoaderOverlay'));

const RequestView = () => {
    const {id} = useParams();
    const [request, setRequest] = useState(null);
    const [messages, setMessages] = useState(null);
    const [loading, setLoading] = useState(true);
    const [messagesLoading, setMessagesLoading] = useState(true);

    const fetchRequest = () => fetch(`/api/requests/${id}/`)
        .then((response) => {
            if (response.status === 200) {
                return response.json();
            }
            return new Promise((resolve) => {
                resolve([]);
            });
        })
        .then((data) => {
            setRequest(data);
            setLoading(false);
        });

    const fetchMessages = () => fetch(`/api/request_messages/?request=${id}`)
        .then((response) => {
            if (response.status === 200) {
                return response.json();
            }
            return new Promise((resolve) => {
                resolve([]);
            });
        })
        .then((data) => {
            setMessages(data);
            setMessagesLoading(false);
        });

    useEffect(() => {
        fetchRequest();
        fetchMessages();
    }, []);

    if (loading) {
        return <LoaderOverlay content="Fetching request ..."/>;
    }

    return (
        <Segment style={{background: 'white'}}>

            <Grid columns={2}>
                <Grid.Row>
                    <Grid.Column>
                        <Header as="h1">
                            <StatusLabel status={request.status}/>
                            {request.title}
                            <Header.Subheader>
                                <OriginIcon origin={request.origin}/>
                                <Moment locale="fr" format="LLLL">{request.created}</Moment>
                                <Label>
                                    <Moment to={request.created}/>
                                </Label>
                            </Header.Subheader>
                            <Header.Subheader>
                                <Icon name="building"/>
                                {request.asso.shortname}
                            </Header.Subheader>
                            <Header.Subheader>
                                <Icon name="user"/>
                                {request.user.full_name}
                            </Header.Subheader>
                        </Header>
                    </Grid.Column>
                    <Grid.Column style={{textAlign: "right"}}>
                        <RequestStatusSelector/>
                    </Grid.Column>
                </Grid.Row>

            </Grid>


            {
                messagesLoading ? (
                    <LoaderOverlay content="Loading messages ..."/>
                ) : (
                    <RequestMessagesFeed messages={messages}/>
                )
            }
            <RequestMessageForm
                request={request}
                onSubmit={() => {
                    fetchMessages();
                }}
            />
        </Segment>
    )
        ;
};

export default RequestView;
