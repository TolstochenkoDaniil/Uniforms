<template>
    <div class="discipline-form-container">
        <h2 class="discipline-name">{{ disciplineName }}</h2>
        <FormList :forms="forms"/>
    </div>
</template>

<script>
import { computed, onMounted } from 'vue';
import { useStore } from 'vuex';
import { useRoute } from 'vue-router';

import FormList from '../components/FormList.vue'

export default {
    name: 'Discipline',
    components: {
        FormList
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