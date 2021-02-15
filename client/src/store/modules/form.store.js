import axios from 'axios';
import { axiosDefaultBaseURL } from '../../appVariables';

const state = {
    form: {
        name: '',
        url: '',
        edit_url: '',
        university: '',
        discipline: ''
    },
    status:''
};

const getters = {
    userForm: state => state.form,
    status: state => state.status
};

const actions = {
    async GET_USER_FORM({ commit, dispatch }, { userId }) {
        return new Promise((resolve, reject) => {
            commit('GET_USER_FORM');
            axios.get(
                `${axiosDefaultBaseURL}/api/v1/${userId}/form`,
                { headers: { Authorization: `Bearer ${localStorage.getItem('user-token')}` }}
            )
            .then(resp => {
                const formParams = resp.data.form_params;
                commit('GET_USER_FORM_SUCCESS');
                dispatch('SET_FORM_PARAMS', formParams);
                resolve(resp);
            })
            .catch(err => {
                console.log(`Error in action: ${err}`)
                commit('GET_USER_FORM_FAILED');
                reject(err);
            })
        })
    },
    async SAVE_USER_FORM({ commit }, { userId, formParams }) {
        return new Promise((resolve, reject) => {
            commit('SAVE_USER_FORM');
            axios.post(
                `${axiosDefaultBaseURL}/api/v1/${userId}/form`,
                { form_params: formParams },
                { headers: { Authorization: `Bearer ${localStorage.getItem('user-token')}` }}
            )
            .then(resp => {
                const status = resp.data.status;
                commit('SAVE_USER_FORM_SUCCESS', status);
                resolve(resp);
            })
            .catch(err => {
                console.log(`Error in action: ${err}`)
                commit('SAVE_USER_FORM_FAILED');
                reject(err);
            })
        })
    },
    SET_FORM_PARAMS({ commit }, formParams) {
        commit('SET_FORM_PARAMS', formParams);
    }
};

const mutations = {
    GET_USER_FORM(state) {
        state.status = 'loading';
    },
    GET_USER_FORM_SUCCESS(state) {
        state.status = 'success';
    },
    GET_USER_FORM_FAILED(state) {
        state.status = 'failed';
    },
    SAVE_USER_FORM(state) {
        state.status = 'pending';
    },
    SAVE_USER_FORM_SUCCESS(state, status) {
        state.status = status;
    },
    SAVE_USER_FORM_FAILED(state) {
        state.status = 'failed';
    },
    SET_FORM_PARAMS(state, formParams) {
        state.form = formParams;
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
};