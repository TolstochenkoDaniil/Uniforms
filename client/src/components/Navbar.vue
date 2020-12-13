<template>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-primary">
        <a class="navbar-brand" href="/">
            <img src="../assets/ulogo.png" alt="Uniforms logo" width="80" height="60">
            <span class="site-name">{{ name }}</span>
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <router-link :to="{ name: 'Login' }" class="nav-link">Вход 
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link :to="{ name: 'Disciplines' }" class="nav-link">Направления
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link :to="{ name: 'Options' }" class="nav-link">Настройки
                    </router-link>
                </li>
                <li class="nav-item">
                    <a class="nav-link disabled" href="#" aria-disabled="true">Статистика</a>
                </li>
                <li class="nav-item">
                    <a class="nav-link disabled" href="#" aria-disabled="true">Правила</a>
                </li>
            </ul>
        </div>
    </nav>
</template>>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
    name: "Navbar",
    props: {
        name: String
    },
    setup() {
        const store = useStore();
        const isAuthenticated = computed(() => store.getters['auth/isAthenticated']);

        const logout = () => {
            store.dispatch('auth/AUTH_LOGOUT');
        }

        return {
            isAuthenticated, 
            logout
        }
    }
}
</script>>

<style>
header
{
    width: 100%;
    background-color: #0c6aed;
}
a.logo 
{
    text-decoration: none;
}
span.site-name
{
    color:aliceblue;
    margin: 1em;
}
#nav a
{
    color: aliceblue;
    text-decoration: none;
}
</style>>