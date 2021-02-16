<template>
    <div class="container d-flex justify-content-center">
        <div class="row">
            <div class="col-12 mx-md-auto">
                <div class="card" style="width: 20rem;">
                    <div v-if="isAuthenticated" class="card-body">
                        Добро пожаловать на Uniforms {{ user.username }}!
                    </div>
                    <div v-else class="card-body">
                        Добро пожаловать на Uniforms!
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import { computed } from 'vue';
import { useStore } from 'vuex';

export default {
  name: 'Home',
  components: {
  },
  setup() {
    const store = useStore();

    const isAuthenticated = computed(() => store.getters['auth/isAuthenticated'])
    const user = computed(() => store.getters['auth/user']);

    return {
      isAuthenticated,
      user
    }
  }
}
</script>
