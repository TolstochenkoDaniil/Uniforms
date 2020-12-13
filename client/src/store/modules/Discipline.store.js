const state = {
    disciplines: [
        {
            name: "Бизнес / Менеджмент",
            route: "business"
        },
        {
            name: "Государственное управление",
            route: "public-administration"
        },
        {
            name: "Дизайн",
            route: "design"
        },
        {
            name: "Журналистика",
            route: "journalistic"
        },
        {
            name: "Искусствоведение",
            route: "art"
        },
        {
            name: "История",
            route: "history"
        },
        {
            name: "Культурология",
            route: "culture"
        },
        {
            name: "Лингвистика",
            route: "linguistics"
        },
        {
            name: "Маркетинг",
            route: "marketing"
        },
        {
            name: "Медиа",
            route: "media"
        },
        {
            name: "Педагогика",
            route: "pedagogy"
        },
        {
            name: "Политология",
            route: "political-science"
        },
        {
            name: "Право",
            route: "law"
        },
        {
            name: "Психология",
            route: "psychology"
        },
        {
            name: "Социология",
            route: "sociology"
        },
        {
            name: "Туризм",
            route: "tourism"
        },
        {
            name: "Урбанистика",
            route: "urbanism"
        },
        {
            name: "Экономика / Финансы",
            route: "economics-finance"
        },
        {
            name: "Философия",
            route: "philosophy"
        },
        {
            name: "Филология",
            route: "philology"
        },
        {
            name: "Другое",
            route: "other"
        },
    ]
}

const getters = {
    getDisciplines(state) {
        return state.disciplines
    }
}

const mutations = {}

const actions = {}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}