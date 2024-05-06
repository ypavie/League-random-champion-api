<<<<<<< HEAD
import { createApp } from 'vue'
import App from './App.vue'
import './assets/tailwind.css'
import { createRouter, createWebHistory } from 'vue-router'
import './assets/tailwind.css'


if ('serviceWorker' in navigator) {
    window.addEventListener('load', function () {
        navigator.serviceWorker.register('/service-worker.js').then(function (registration) {
            console.log('ServiceWorker registration successful with scope: ', registration.scope);
        }, function (err) {
            console.error('ServiceWorker registration failed: ', err);
        });
    });
}

=======
import '@picocss/pico/css/pico.min.css'
import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
>>>>>>> main

const router = createRouter({
    history: createWebHistory(),
    routes: [
        { path: '/', component: App },
        { path: '/:id', component: App }
    ]
})

<<<<<<< HEAD
const app = createApp(App)

app.use(router)
app.mount('#app')
=======
createApp(App)
    .use(router) // Use the router
    .mount('#app')
>>>>>>> main
