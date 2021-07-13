import { GET_LEADS, DELETE_LEAD, ADD_LEAD, GET_ERRORS } from "./types";
import { createMessage } from './messages';


async function promiseHandling (response) {
    const data = await response.json();
    const status = response.status;
    return {msg: data, status}
    }


function handleResponse(response) {
    if (!response.ok) {
        throw response
    }
    return response;
}

// GET LEADS
export const getLeads = () => dispatch => {
    fetch ("/api/leads/")
    .then(handleResponse)
    .then(response => response.json())
    .then(data => {
        dispatch ({
            type: GET_LEADS,
            payload: data,
        });
    })
    .catch (error => console.log(error));
}


// DELETE LEAD
export const deleteLead = (id) => dispatch => {
    fetch(`/api/leads/${id}/`, { method: 'DELETE'})
    .then(handleResponse)
    .then(() => {
        dispatch (createMessage({ deleteLead: "Lead Deleted"}));
        dispatch ({
                    type: DELETE_LEAD,
                    payload: id,
                });
    })
    .catch ((error) => console.log (error));
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
    .then(handleResponse)
    .then(response => response.json())
    .then(data => {
        dispatch (createMessage({addLead: "Lead Added"}));
        dispatch ({
            type: ADD_LEAD,
            payload: data,
        });
    })
    .catch(response => {
            promiseHandling(response)
            .then(errors => {dispatch({
                                type: GET_ERRORS,
                                payload: errors
                });
            });
        });
};
