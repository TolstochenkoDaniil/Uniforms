<template>
    <div class="options-page">
        <ul class="form-option">
            <li class="form-option-name">
                <input type="text" v-model="form.name" placeholder="Название опроса">
            </li>
            <li class="form-option-url">
                <input type="text" v-model="form.url" placeholder="Ссылка на google forms">
            </li>
            <li class="form-option-edit-url">
                <input type="text" v-model="form.edit_url" placeholder="Ссылка для редактирования google forms">
            </li>
            <li class="form-option-university">
                <select v-model="form.university">
                    <option disabled value="">
                        Выберите свой университет
                    </option>
                    <option v-for="(university, index) in universityList" :key="index" :value="university">
                        {{ university }}
                    </option>
                </select>
            </li>
            <li class="form-option-descipline">
                <select v-model="form.discipline">
                    <option disabled value="">
                        Выберите направление
                    </option>
                    <option v-for="(discipline, index) in disciplines" :key="index" :value="discipline.route">
                        {{ discipline.name }}
                    </option>
                </select>
            </li>
        </ul>
        <button v-on:click="saveForm(form)" class="submit-form-options">
            Coxpaнить
        </button>
    </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useStore } from 'vuex';

export default {
    name: 'Options',

    async setup() {
        const store = useStore();

        const user = computed(() => store.getters['auth/user']);
        const form = computed(() => store.getters['form/userForm']);
        const status = computed(() => store.getters['form/status']);
        const disciplines = computed(() => store.getters['disciplines/list']);

        async function saveForm(form) {
            await store.dispatch('form/SAVE_USER_FORM', { userId: user.value.pk, formParams: form});
        }

        const fetchForm = async () => {
            await store.dispatch('form/GET_USER_FORM', { userId: user.value.pk })
        }

        onMounted(async () => {
            if (user.value !== 'undefined')
                await fetchForm();
        });

        return {
            disciplines,
            form,
            status,
            saveForm,
            universityList: computed(() => store.getters['university/list'])
        }
    }
}
</script>

<style>
div.options-page
{
    display: table;
    margin-right: auto;
    margin-left: auto;
}
ul.form-option
{
    padding: 50px 10px 10px 10px;
    text-decoration: none;
    list-style-type: none;
}
li[class^="form-option-"]
{
    padding: 10px;
    width: 300px;
    height: 50px;
    text-decoration: none;
}
.submit-form-options
{
    padding: 0;
    width: 200px;
    height: 30px;
}
input
{
    width: 280px;
}
select
{
    width: 280px;
}
</style>