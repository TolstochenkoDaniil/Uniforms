<template>
    <router-link :to="{ name: 'discipline', params: { discipline: block.route, disciplineName: block.name }}" class="discipline">
        <div v-if="typeof block.route !== 'undefined'" class="discipline-block">
            <p>{{ block.name }}</p>
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
}
</script>

<style>
div.discipline-block
{
    margin: 0px;
    
    text-align: center;
    padding: 20px;
    width: 280px;
    height: 65px;
    background: #0c6aed;
    border-radius: 20px;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}
div.discipline-block:hover
{
    background: #faaf46;
}
a.discipline
{
    text-decoration: none;
    color: whitesmoke;
}
p
{
    margin: 14px;
}    
</style>