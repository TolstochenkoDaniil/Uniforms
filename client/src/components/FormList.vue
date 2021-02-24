<template>
    <ul class="form-list">
        <li v-for="(form, index) in forms" :key="index" :class="{['form-'+index]: true}">
            <Form :form="form"></Form>
        </li>
    </ul>
</template>>

<script>
import Form from './Form.vue'

export default {
    name: 'FormList',
    components: {
        Form,
    },
    props: {
        forms: Array
    }
}
</script>

<style>
ul.form-list
{
    position: absolute;
    top: 20%;
    left: 40%;
    margin: 0px;
    padding: 0px;
    display: table-cell;
    text-align:center;
    text-decoration: none;
    list-style-type: none;

}
li[class^='form-']
{
    margin: auto;
    padding: 2px;
    height: auto;
    width: 420px;
}
</style>