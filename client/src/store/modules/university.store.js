const state = {
    university: [
        'ВШЭ'
    ]
};

const getters = {
    list: state => state.university
}

export default {
    namespaced: true,
    state,
    getters
};