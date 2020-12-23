import axios from 'axios';
import { axiosDefaultBaseURL } from '../../appVariables';

const state = {
    form_params: {},
    status:''
}

const getters = {
    form_params: state => state.form_params,
    status: state => state.status
}

const actions = {
    GET_USER_FORM({ commit, dispatch }, { userId }) {
        return new Promise((resolve, reject) => {
            commit('GET_USER_FORM');
            axios.get(`${axiosDefaultBaseURL}/api/v1/${userId}/form`)
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
    SAVE_USER_FORM({ commit }, { userId, formParams }) {
        return new Promise((resolve, reject) => {
            commit('SAVE_USER_FORM');
            axios.post(`${axiosDefaultBaseURL}/api/v1/${userId}/form`, {
                form_params: formParams
            })
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
    SET_FORM_PARAMS({ commit }, { formParams }) {
        commit('SET_FORM_PARAMS', formParams);
    }
}

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
        state.form_params = formParams;
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}