<template>
    <table class="discipline-table">
        <tr class="table-row" v-for="(row, row_index) in tableRows()" :key="row_index" >
            <td :class="{['column-'+col]: true}" v-for="(col, index) in tableColumns" :key="index">
                <DisciplineBlock :block="disciplineList.shift()"></DisciplineBlock>
            </td>
        </tr>
    </table>
</template>

<script>
import { ref, computed, onBeforeMount } from 'vue';
import { useStore } from 'vuex';

import DisciplineBlock from './DisciplineBlock.vue';

function createCopy(array) {
    return Array.from(array);
}

export default {
    name: "DisciplineTable",
    components: {
        DisciplineBlock,
    },
    setup() {
        const tableColumns = ref([1,2]);
        const tableRows = () => {
            const tableRows = Math.round(disciplines.value.length / tableColumns.value.length);
          
            return tableRows
        };
        
        const store = useStore();
        const disciplines = computed(() => store.state.discipline.disciplines);
        const disciplineList = createCopy(disciplines.value);
        
        onBeforeMount(() => {
            disciplineList.push(createCopy(disciplines.value));
        })

        return {
            tableColumns,
            tableRows,
            disciplineList
        }
    },
}
</script>

<style>
div.discipline-table
{
    padding: 10px;
    margin: 0px;
}
table.discipline-table
{
    margin-top: 20px;
    margin-left: auto;
    margin-right: auto;
    padding: 2px;
    border: none;
    position: relative;
}
td[class^="column-"]
{
    margin: 0;
    padding-left: 50px;
    padding-right: 50px;
    padding-top: 20px;
    padding-bottom: 20px;
    text-align: center;
}
div.discipline-block
{
    padding: 5px;
}
</style>