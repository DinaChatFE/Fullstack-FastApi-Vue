import axiosInstance from "./AxiosTokenInstance";
import { BASE_URL } from "@/store//storeconstants";

class UserDataService {
    getAll() {
        return axiosInstance.get(BASE_URL + "auth/all?all_role=true");
    }
    get(id) {
        return axiosInstance.get(BASE_URL + `auth/all/${id}`);
    }
    profile(){
        return axiosInstance.get(BASE_URL + `auth/user-profile`);
    }
    create(data) {
        return axiosInstance.post(BASE_URL + "auth/register", data);
    }
    update(id, data) {
        return axiosInstance.put(BASE_URL + `auth/update/${id}`, data);
    }
    delete(id) {
        return axiosInstance.delete(BASE_URL + `user/${id}`);
    }
    deleteAll() {
        return axiosInstance.delete(`user`);
    }
    findByTitle(title) {
        return axiosInstance.get(`user?title=${title}`);
    }
}
export default new UserDataService();