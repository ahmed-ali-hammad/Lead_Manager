import axios from 'axios';
import { GET_LEADS, DELETE_LEAD, ADD_LEAD } from "./types";


// GET LEADS
export const getLeads = () => dispatch => {
    axios
    .get ("/api/leads/")
    .then((res) => {
        dispatch ({
            type: GET_LEADS,
            payload: res.data,
        });
    })
    .catch ((err) => console.log (err));
}

// DELETE LEAD
export const deleteLead = (id) => dispatch => {
    const requestOptions = {
        method: 'DELETE',
    }

    fetch(`/api/leads/${id}/`, requestOptions)
    .then((res) => {
        dispatch ({
            type: DELETE_LEAD,
            payload: id,
        });
    })
    .catch ((err) => console.log (err));
}


//ADD LEAD
export const addLead = (lead) => dispatch => {
    const requestOptions = {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify(lead)
    };

    fetch(`/api/leads/`, requestOptions)
    .then((res) => res.json())
    .then((data) => {
        dispatch ({
            type: ADD_LEAD,
            payload: data,
        });
    })
    .catch ((err) => console.log (err));
}






