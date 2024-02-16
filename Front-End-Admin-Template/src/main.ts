import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import './assets/base.css'
import './assets/main.css'
import PrimeVue from 'primevue/config';
import DashboardLayout from './components/DashboardLayout.vue'
import EmptyLayout from './components/EmptyLayout.vue'
import Button from 'primevue/button';
// @ts-ignore
import Lara from './presets/lara/lara'

const app = createApp(App)

app.component('DefaultLayout', DashboardLayout)
app.component('EmptyLayout', EmptyLayout)

app.use(router)
app.use(PrimeVue, {
    unstyled: true,
    pt: Lara
});
app.component('Button', Button);
app.mount('#app')
