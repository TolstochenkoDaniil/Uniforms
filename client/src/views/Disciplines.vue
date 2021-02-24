<template>
    <div class="discipline-table">
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
import DisciplineBlock from '../components/DisciplineBlock.vue'

export default {
    name: "Disciplines",
    components: {
        DisciplineBlock
    },
    setup() {
        const store = useStore();
        const disciplines = computed(() => store.getters['disciplines/list'])

        return {
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
</style>>