<template>
    <nav class="navbar navbar-expand-md navbar-dark fixed-top bg-primary">
        <router-link :to="{ name: 'Home' }" class="nav-brand">
            <img src="../assets/ulogo.png" alt="Uniforms logo" width="80" height="60">
            <span class="site-name">{{ name }}</span>
        </router-link>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item active">
                    <div v-if="!userAuthenticated">
                        <router-link v-on:click.once="googleSignIn" :to="{ name: 'Home' }" class="nav-link">Вход 
                        </router-link>
                    </div>
                    <div v-else>
                        <router-link v-on:click.once="logout" :to="{ name: 'Home' }" class="nav-link">Выход
                        </router-link>
                    </div>
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
import gAuth from 'vue3-google-auth';

export default {
    name: "Navbar",
    props: {
        name: String
    },
    setup() {
        const $gAuth = gAuth.useGAuth();
        const store = useStore();

        const userAuthenticated = computed(() => store.getters['auth/isAuthenticated'])

        const googleSignIn = () => {
            $gAuth.signIn()
            .then(resp => {
                const token = resp.uc.access_token;
                store.dispatch('auth/AUTH_REQUEST', { 
                    accessToken: token,
                    provider:'google' 
                });
            })
            .catch(err => {
                console.log(`Auth error: ${err}`);
            })
        }
        const logout = () => {
            store.dispatch('auth/AUTH_LOGOUT');
        }

        return { 
            googleSignIn,
            logout, 
            userAuthenticated,
        }
    }
}
</script>>

<style>
.navbar
{
    padding: 0.5em;
}
header
{
    width: 100%;
    background-color: #0c6aed;
}
a.logo 
{
    text-decoration: none;
}
a.nav-brand
{
    color: aliceblue;
    text-decoration: none;
    margin: 0.1em;
}
.site-name
{
    margin: 1em;
}
</style>>