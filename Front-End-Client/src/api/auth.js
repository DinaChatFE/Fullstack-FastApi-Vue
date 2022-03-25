import axios from "axios";


const baseLink = process.env.VUE_APP_API;

export default {

    login(payload = {}, cb, cbError) {
        axios.post(`${baseLink}auth/login`, payload).then(response => {
            cb(response)
        }).catch((error) => cbError(error))
    },
    getProfile(token, cb, cbError) {
        axios.get(`${baseLink}auth/user-profile`, { headers: { Authorization: `Bearer ${token}` } },).then(response => {
            cb(response)
        }).catch(error => {
            cbError(error)
        })
    },
    register(body = {}, cb, cbError) {
        axios.post(`${baseLink}auth/register`, body).then(response => {
            cb(response)
        }).catch(error => {
            cbError(error)
        })
    },
    updateUser(body, token , cb, cbError) {
        axios.put(`${baseLink}auth/update/${body.id}`, body, { headers: { Authorization: `Bearer ${token}` } }).then(res => cb(res), (error) => cbError(error));
    },
    getAll(token, cb, cbError){
        axios.get(`${baseLink}auth/all`, {headers: {Authorization: `Bearer ${token}`}}).then((res=> cb(res)), error=> cbError(error))
    }
}