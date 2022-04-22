import React, { useState } from 'react'
import {Dropdown} from 'semantic-ui-react'

const options = [
    {key: 1, text: 'Open', value: 'OPEN'},
    {key: 2, text: 'Assigned', value: 'ASSIGNED'},
    {key: 3, text: 'Closed', value: 'CLOSED'},
    {key: 4, text: 'Done', value: 'DONE'},
    {key: 5, text: 'Waiting for tech', value: 'WAITING_TECH'},
    {
        key: 6,
        text: 'Waiting for tiers service',
        value: 'WAITING_FOR_TIERS_SERVICE',
    },
    {key: 7, text: 'Waiting for customer', value: 'WAITING_FOR_CUSTOMER'},
]




const RequestStatusSelector = (onChange) => {
    const [status, setStatus]=useState("OPEN");
    const handleChange = (e, v) => {
    setStatus(v.value);
    onChange(v.value);
};



    return (<Dropdown options={options} value={status} selection/>)
}
export default RequestStatusSelector