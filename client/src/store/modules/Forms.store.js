const state = {
    forms: [
        {
            id: 1,
            name: 'Вы любите Насвай?',
            description: 'Мы хотим узнать, как много людей являются настоящими ценителями прекрасного...',
            university: 'Вселенский Университет',
            user: 'Дед',
            date: '6.06.2066',
        },
        {
            id: 2,
            name: 'Продам жигу',
            description: 'Отдам любимую лайбочку в хорошие руки',
            university: 'Лучшая школа - это двор',
            user: 'Риос',
            date: '10.10.2020',
        },
        {
            id: 3,
            name: 'Опрос от WAB',
            description: 'Какой видос на моем канале больше зашел?',
            university: 'Универы для лохов',
            user: 'Bach101',
            date: '15.03.2020',
        },
        {
            id: 4,
            name: 'Крок &#x1F4A9; ?',
            description: 'Хочу знать ваше мнение, хотя мне похуй',
            university: 'Высшая школа превосходства',
            user: 'Амиго69',
            date: '29.08.2020',
        },
    ]
}

const getters = {
    getForms(state) {
        return state.forms
    }
}

const mutations = {
    addForm(state, form) {
        form.id = state.forms.length
        state.forms.push(form)
        console.log("Mutation was called")
    }
}

const actions = {
    addForm({ commit }, form) {
        commit('addForm', form)
        console.log("Action was called")
    }
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}