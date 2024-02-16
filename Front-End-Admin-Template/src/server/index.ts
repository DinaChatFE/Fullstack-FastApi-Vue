import axios from "axios";

export default function() {
    const instance = axios.create({
        baseURL: import.meta.VUE_APP_API ?? 'https://api-event.dinadev.pro/'
    })

    return instance;
}