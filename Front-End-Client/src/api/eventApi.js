import axios from "axios"


const baseUrl = process.env.VUE_APP_API


export default {
    header: (token) => {
        return {
            Authorization: `Bearer ${token}`,
        }
    },
    getAllEvent: (queryParams = [], payload = '', page = 1, token, cb, cbError) => {
        let query = ''
        let user_token = ''
        if (payload) user_token = `&user=${payload}`
        queryParams.forEach(val => {
            query += `&${val.key}=${val.value}`
        });
        axios.get(`${baseUrl}event?page=${page}&page_size=12${query}${user_token}`, { headers: { Authorization: `Bearer ${token}` } }).then(response => cb(response)
        ).catch(error => cbError(error))
    },
    filterEvent(queryParams = {}, page = 1, token, cb, cbError) {
        let query = ''
        queryParams.forEach(val => {
            query += `&${val.key}=${val.value}`
        });
        console.log(query);
        axios.get(`${baseUrl}event?page=${page}&page_size=12${query}`, { headers: { Authorization: `Bearer ${token}` } }).then(response => cb(response)).catch(error => cbError(error))
    },
    filterByEventInterested(token, page = 1, cb, cbError) {
        axios.get(`${baseUrl}event/by-interested?page=${page}&page_size=12&user=${token}`).then(res => cb(res), error => cbError(error))
    },

    postPreference(payload, token, cb, cbError) {

        axios.get(`${baseUrl}event/preference/${payload.id}?is_interested=${payload.is_interested}`, { headers: { Authorization: `Bearer ${token}` } }).then(res => cb(res)).catch(error => cbError(error))
    },
    getDetail(id, token, cb, cbError) {
        if (!token) {
            token = ''
        }
        axios.get(`${baseUrl}event/${id}?token=${token}`, { headers: { Authorization: `Bearer ${token}` } }).then(res => cb(res), error => cbError(error))
    },
    registerEventApi(id, token, cb, cbError) {
        axios.post(`${baseUrl}registration/${id}`, {}, { headers: { Authorization: `Bearer ${token}` } }).then(res => cb(res), error => cbError(error))
    }
}