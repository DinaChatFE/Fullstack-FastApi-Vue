import { createApp } from "vue";
import App from "./App.vue";
import { createStore } from "vuex";
import "./index.css";
import products from "./store/modules/products";
import auth from './store/modules/auth'
import route from './router'
import event from './store/modules/event'
import Notifications from '@kyvg/vue3-notification'
import news from './store/modules/news'
import categories from './store/modules/categories'
import VueSweetalert2 from 'vue-sweetalert2';
import 'sweetalert2/dist/sweetalert2.min.css';

const store = createStore({
  modules: {
    products,
    auth,
    event,
    news,
    categories
  },
});

createApp(App)
  .use(route)
  .use(store)
  .use(Notifications)
  .use(VueSweetalert2)
  .mount("#app");
