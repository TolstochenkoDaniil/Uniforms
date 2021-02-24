<template>
    <div class="container justify-content-center">
        <div class="row justify-content-center p-1 m-1 mb-5">
            <div class="col-mx-12">
                <figure class="text-center">
                    <h1 class="display-1">
                        <p>Делитесь опросами<br>
                        со всеми потоками &#10024;</p>
                    </h1>
                </figure>
            </div>
        </div>
        <div class="row justify-content-center p-1 m-1">
            <div class="col-mx-12">
                <container>
                    <div v-for="(discipline, index) in disciplines" :key=index class="discipline-parent">
                        <DisciplineBlock :block="discipline"></DisciplineBlock>
                    </div>
                </container>
            </div>
        </div>
    </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import DisciplineBlock from '../components/DisciplineBlock.vue';

export default {
    name: 'Home',
    components: {
        DisciplineBlock,
    },
    setup() {
        const store = useStore();

        const isAuthenticated = computed(() => store.getters['auth/isAuthenticated'])
        const user = computed(() => store.getters['auth/user']);
        const disciplines = computed(() => store.getters['disciplines/list'])
        return {
            isAuthenticated,
            user,
            disciplines
        }
    }
}
</script>

<style>
container {
    display: grid;
    place-items: center;
    grid-template-columns: repeat(2, 1fr);
    grid-gap: 3em;
    box-sizing: border-box;
    height: auto;
    width: 100%;
    padding: 1em;
}

.discipline-parent {
    display: grid;
    place-items: center;
    height: auto;
}

</style>
