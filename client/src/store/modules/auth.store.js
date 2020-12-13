import axios from 'axios';
import router from '../../router/index';
import { axiosDefaultsBaseURL } from '../../appVariables';

const state = {
    token: localStorage.getItem('user-token') || '',
    refreshToken: localStorage.getItem('user-refresh-token') || '',
    status: '',
    user: JSON.parse(localStorage.getItem('user')) || {}
}

const getters = {
    isAuthenticated: state => !!state.token,
    authStatus: state => state.status,
    user: state => state.user
}

const actions = {
    AUTH_REQUEST({ commit, dispatch }, { accessToken, provider }) {
        return new Promise((resolve, reject) => {
            commit('AUTH_REQUEST');
            axios.post(`${axiosDefaultsBaseURL}/auth/${provider}`, {
                access_token: accessToken
            })
            .then(resp => {
                const token = resp.data.access_token;
                localStorage.setItem('user-token', token);
                commit('AUTH_SUCCESS', token);
                dispatch('USER_REQUEST', resp.data.user);
                resolve(resp);
            })
            .catch(err => {
                console.log(`Error in action: ${err}`)
                commit('AUTH_ERROR', err);
                localStorage.removeItem('user-token');
                reject(err);
            })
        })
    },
    AUTH_LOGOUT({ commit, dispatch }) {
        return new Promise((resolve, reject) => {
            commit('AUTH_LOGOUT');
            localStorage.removeItem('user-token');
            localStorage.removeItem('user');
            resolve();
        })
    },
    USER_REQUEST({ commit }, user) {
        commit('USER_REQUEST', user);
    }
}

const mutations = {
    AUTH_REQUEST(state) {
        state.status = 'loading';
    },
    AUTH_SUCCESS(state, token) {
        state.token = token;
        state.status = 'success';
    },
    AUTH_ERROR(state, err) {
        state.status = String(err);
    },
    AUTH_LOGOUT(state) {
        state.token = '';
        state.user = '';
        state.status = 'logout';
        router.push('/');
    },
    USER_REQUEST(state, user) {
        state.user = user;
        localStorage.setItem('user', JSON.stringify(user));
        router.push('/');
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}