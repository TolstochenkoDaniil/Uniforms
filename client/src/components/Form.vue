<template>
    <!-- <router-link :to="{ name: 'form', params: {form_id: form.id}}" class="form"> -->
        <div class="form-card">
            <h3 class="form-name">{{ form.name }}</h3>
            <ul class=form-credentials>
                <li><a v-bind:href="form.url">Начать опрос</a></li>
            </ul>
        </div>
    <!-- </router-link> -->
</template>

<script>
export default {
    name: 'Form',
    props: {
        form: {
            id: Number,
            name: String,
            url: String
        }
    }
}
</script>

<style>
div.form-card
{
    margin: 10px;
    text-align: left;
    padding: 10px;
    width: 400px;
    height: 250px;
    background: #0c6aed;
    border-radius: 30px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
h3.form-name
{
    margin: 5px;
}
p.form-description
{
    margin-top: 20px;
    margin: 10px;
}
ul.form-credentials
{
    margin: 5px;
    text-decoration: none;
    list-style-type: none;
}
a.form
{
    text-decoration: none;
    color: whitesmoke;
}
</style>

