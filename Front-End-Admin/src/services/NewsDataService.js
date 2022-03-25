import axiosInstance from "./AxiosTokenInstance";
import { BASE_URL } from "@/store//storeconstants";

class NewsDataService {
    getAll() {
        return axiosInstance.get(BASE_URL + "news");
    }
    get(id) {
        return axiosInstance.get(BASE_URL + `news/${id}`);
    }
    create(data) {
        return axiosInstance.post(BASE_URL + "news", data);
    }
    update(id, data) {
        return axiosInstance.put(BASE_URL + `news/${id}`, data);
    }
    delete(id) {
        return axiosInstance.delete(BASE_URL + `news/${id}`);
    }
    deleteAll() {
        return axiosInstance.delete(`news`);
    }
    findByTitle(title) {
        return axiosInstance.get(BASE_URL + `news?title=${title}`);
    }
}
export default new NewsDataService();