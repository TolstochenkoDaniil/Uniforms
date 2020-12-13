<template>
    <div class="options-page">
        <ul class="form-option">
            <li class="form-option-name">
                <input type="text" v-model="form.name" placeholder="Название опроса">
            </li>
            <li class="form-option-url">
                <input type="text" v-model="form.url" placeholder="Ссылка на google forms">
            </li>
            <li class="form-option-university">
                <select v-model="form.university">
                    <option disabled value="">
                        Выберите свой университет
                    </option>
                </select>
            </li>
            <li class="form-option-descipline">
                <select v-model="form.discipline">
                    <option disabled value="">
                        Выберите направление
                    </option>
                    <option v-for="(discipline, index) in disciplines" :key="index" :value="discipline.name">
                        {{ discipline.name }}
                    </option>   
                </select>
            </li>
        </ul>
    <button v-on:click.once="registerForm(form)" class="submit-form-options">
        Coxpaнить
    </button>
    </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
    name: 'Options',

    setup() {
        const store = useStore();
        const disciplines = computed(() => store.state.Discipline.disciplines)
        const form = {
            name: "",
            url: "",
            university: "",
            discipline: ""
        };

        function registerForm(form) {
            console.log("Adding form "+JSON.stringify(form));
            store.dispatch('Forms/addForm', form);
            alert("Form was added!");
        }

        return { 
            disciplines,
            form,
            registerForm 
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