import axios from "axios"
import store from "../store/store";
import { GET_USER_TOKEN_GETTER, BASE_URL } from "../store/storeconstants";

const axiosInstance = axios.create({});

axiosInstance.interceptors.request.use(request => {
    let token = store.getters[`auth/${GET_USER_TOKEN_GETTER}`];
    request.headers.common['Authorization'] = `Bearer ${token}`;
    request.headers.common['Content-Type'] = `application/json`;
    request.headers.common['Access-Control-Allow-Origin'] = `*`;
    return request;
});

export default axiosInstance;
