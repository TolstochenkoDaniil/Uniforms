import { createApp } from 'vue';

import jQuery from 'jquery';
import 'popper.js';
import 'bootstrap';
import 'bootstrap/dist/css/bootstrap.css';

import App from './App.vue';
import router from './router';
import store from './store';

import axios from 'axios';
import { axiosDefaultBaseURL, oauthGoogle } from './appVariables';
import gAuth from 'vue3-google-auth';

window.$ = window.jQuery = jQuery;

axios.defaults.baseURL = axiosDefaultBaseURL;

const $gAuth = gAuth.createGAuth({
    clientId: oauthGoogle,
    scope: 'profile email',
    prompt: 'select_account'
})

const app = createApp(App);
app.use($gAuth);
app.use(store);
app.use(router);
app.mount('#app');
