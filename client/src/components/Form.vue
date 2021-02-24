<template>
    <div class="card">
        <h3 class="name">{{ form.name }}</h3>
        <div class="body">
            <a v-bind:href="form.url" class="btn btn-primary">Пройти опрос</a>
        </div>
    </div>
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
div.card
{
    margin: 2em;
    padding: 0.5em;
    width: 35em;
    height: auto;
}
.card {
  box-shadow: 0 0.3em 0.5em 0 rgba(0,0,0,0.2);
  transition: 0.3s;
}
.card:hover {
  box-shadow: 0 0.5em 0.8em 0 rgba(0,0,0,0.2);
}
h3.name
{
    margin: 0.7em;
}
a.btn
{

}
</style>

