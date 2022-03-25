import axios from 'axios'

let baseUrl = process.env.VUE_APP_API

export default {
    getAllNews: (queryParams = [], payload = '', page = 1, token, cb, cbError) => {
        let query = ''
        let user_token = ''
        if (payload) user_token = `&user=${payload}`
        queryParams.forEach(val => {
            query += `&${val.key}=${val.value}`
        });
        axios.get(`${baseUrl}news?page=${page}&page_size=12${query}${user_token}`, { headers: { Authorization: `Bearer ${token}` } }).then(response => cb(response)
        ).catch(error => cbError(error))
    },
    getByUser(user_id, page, token, cb, cbError) {
        axios.get(`${baseUrl}news/by-user?user_id=${user_id}&page=${page}`, { headers: { Authorization: `Bearer ${token}` } }).then(res => cb(res)).catch(error => cbError(error))
    },
    getByCategories(cat_id, page, token, cb, cbError) {
        axios.get(`${baseUrl}news/by-categories?cat_id=${cat_id}&page=${page}`, { headers: { Authorization: `Bearer ${token}` } }).then(res => cb(res)).catch(error => cbError(error))
    },
    getDetail(id, token, cb, cbError) {
        axios.get(`${baseUrl}news/${id}`, { headers: { Authorization: `Bearer ${token}` } }).then(res => cb(res), error => cbError(error))
    }
}