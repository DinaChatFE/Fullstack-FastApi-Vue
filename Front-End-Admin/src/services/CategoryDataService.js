import axiosInstance from "./AxiosTokenInstance";
import { BASE_URL } from "@/store//storeconstants";

class CategoryDataService {
    getAll() {
        return axiosInstance.get(BASE_URL + "auth/user-profile");
    }
    get(id) {
        return axiosInstance.get(BASE_URL + `category/${id}`);
    }
    create(data) {
        return axiosInstance.post(BASE_URL + "category", data);
    }
    update(id, data) {
        return axiosInstance.put(BASE_URL + `category/${id}`, data);
    }
    delete(id) {
        return axiosInstance.delete(`user/${id}`);
    }
    deleteAll() {
        return axiosInstance.delete(`user`);
    }
    findByTitle(title) {
        return axiosInstance.get(`user?title=${title}`);
    }
}
export default new CategoryDataService();