import axios from 'axios';
import { axiosDefaultBaseURL } from '../../appVariables';

const state = {
    forms: []
};

const getters = {
    formList: state => state.forms
};

const actions = {
    async GET_FORMS({ commit, dispatch }, { discipline }) {
        return new Promise((resolve, reject) => {
            axios.get(
                `${axiosDefaultBaseURL}/api/v1/forms/${discipline}/list`
            )
            .then(resp => {
                const forms = resp.data.results;
                console.log(resp.data)
                console.log(`Fetched form from api: ${forms}`);
                commit('SET_FORMS', forms);
                resolve(resp);
            })
            .catch(err => {
                reject(err);
            })
        })
    }
};

const mutations = {
    SET_FORMS(state, forms){
        state.forms = forms; 
    }
};

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}