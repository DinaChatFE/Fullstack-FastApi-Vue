import axiosInstance from "./AxiosTokenInstance";
import { BASE_URL } from "@/store//storeconstants";

class EventDataService {
    getAll() {
        return axiosInstance.get(BASE_URL + "event");
    }
    get(event_id) {
        return axiosInstance.get(BASE_URL + `event/${event_id}`);
    }
    getEventForAdmin(event_id) {
        return axiosInstance.get(BASE_URL + `event/admin/${event_id}`);
    }
    create(data) {
        return axiosInstance.post(BASE_URL + "event", data);
    }
    getDashboard(){
        return axiosInstance.get(BASE_URL + 'event/dashboard/all');
    }
    update(id, data) {
        return axiosInstance.put(BASE_URL + `event/${id}`, data);
    }
    checkIn(event_id, user_id) {
        return axiosInstance.post(BASE_URL + `registration/check-in/${event_id}/${user_id}`);
    }
    delete(id) {
        return axiosInstance.delete(BASE_URL + `event/${id}?force=true`);
    }
    deleteAll() {
        return axiosInstance.delete(`user`);
    }
    findByTitle(title) {
        return axiosInstance.get(`user?title=${title}`);
    }
}
export default new EventDataService();