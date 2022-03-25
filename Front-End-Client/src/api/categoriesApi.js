import axios from 'axios'

let baseUrl = process.env.VUE_APP_API

export default {
    getAll: (cb, cbError) => {
        axios.get(`${baseUrl}category`).then(response => cb(response)
        ).catch(error => cbError(error))
    },
}