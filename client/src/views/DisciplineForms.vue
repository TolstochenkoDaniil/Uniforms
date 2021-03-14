<template>
    <div class="discipline-forms justify-content-center ">
        <div class="discipline-forms-header row">
            <div class="discipline-forms-header col-12">
                <figure class="discipline-forms-header text-center">
                    <h2 class="display-2">{{ disciplineName }}</h2>
                </figure>
            </div>
        </div>
        <div class="form row">
            <div class="form col-12 d-flex justify-content-center">
                <div v-for="(form, index) in forms" :key=index class="form">
                    <Form :form="form"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';

import Form from '../components/Form.vue'

export default {
    name: 'Discipline',
    components: {
        Form
    },
    setup() {
        const { params: { discipline, disciplineName }, } = useRoute();
        const store = useStore();
        const forms = computed(() => store.getters['forms/formList']);
        const fetchForms = async () => {
            await store.dispatch('forms/GET_FORMS', { discipline: discipline });
        };

        onMounted(async () => {
            await fetchForms();
        });

        return { disciplineName, forms }
    }
}
</script>

<style>

</style>