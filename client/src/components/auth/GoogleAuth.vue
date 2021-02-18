<template>
    <div class="container d-flex justify-content-center">
        <div class="row">
            <div class="col-12 mx-md-auto">
                <div class="card" style="width: 20rem;">
                    <div v-if="userAuthenticated" class="welcome">
                        <div class="card-body">Добро пожаловать на Uniforms {{ user.username }}!</div>
                        <button  class="btn btn-primary m-2" v-on:click="logout">Logout</button>
                    </div>
                    <div v-else class="login">
                        <div class="card-body">Добро пожаловать на Uniforms!</div>
                        <button class="btn btn-primary m-2" v-on:click.once="googleSignIn">Sign Google</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';
import gAuth from 'vue3-google-auth';
export default {
    name: "GoogleAuth",
    setup() {
        const $gAuth = gAuth.useGAuth();
        const store = useStore();
        const userAuthenticated = computed(() => store.getters['auth/isAuthenticated'])
        const user = computed(() => store.getters['auth/user']);
        const googleSignIn = () => {
            $gAuth.signIn()
            .then(resp => {
                const token = resp.wc.access_token;
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
            user, 
        }
    }
}
</script>

<style>
</style>