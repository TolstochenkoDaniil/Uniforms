<template>
    <router-link :to="{ name: 'discipline', params: { discipline: block.route, disciplineName: block.name }}" class="discipline">
        <div class="container discipline-block justify-content-center">
            <div class="row">
                <div class="col-lg-4">
                    <img :src="`${publicPath}assets/disciplines/${block.route}.ico`" class="img-fluid">
                </div>
                <div class="discipline-name col-lg">
                    <p>{{ block.name }}</p>
                </div>
            </div>
        </div>
    </router-link>
</template>

<script>
export default {
    name: "DisciplineBlock",
    props: {
        block: {
            name: String,
            route: String
        },
    },
    setup() {
        return {
            publicPath: process.env.BASE_URL
        }
    }
}
</script>

<style>
.discipline-block
{
    text-align: center;
    height: 7em;
    width: 25em;
    background: #0c6aed;
    border-radius: 3em;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.discipline-block:hover
{
    background: #faaf46;
}
a.discipline
{
    margin: 0.1em;
    padding: 0.1em;
    text-decoration: none;
    color: whitesmoke;
}
.discipline-name
{
    display: flex;
    flex-direction: column;
    justify-content: center;
}
.discipline-name p
{
    text-align: center;
    margin: 0.1em;
    padding: 0.1em;
}
</style>