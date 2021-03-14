<template>
    <suspense>
        <div id="app">
            <Navbar name="Uniforms.edu"/>
              <router-view :key="$route.fullPath" v-slot="{ Component }">
                <transition name="fade" mode="out-in">
                  <component :is="Component" />
                </transition>
              </router-view>
        </div>
    </suspense>
</template>

<script>
import Navbar from './components/Navbar'

export default {
  name: "App",
  components: {
    Navbar
  }
}
</script>

<style>

#app {
  text-align: center;
  margin-top: 8em;
  box-sizing: border-box;
}
body
{
  font-family: "Open Sans", Arial, sans-serif;
  margin: 0em;
  padding: 0em;
}
.fade-enter-active, .fade-leave-active {
  transition-property: opacity;
  transition-duration: .2s;
}

.fade-enter-active {
  transition-delay: .2s;
}

.fade-enter, .fade-leave-active {
  opacity: 0
}
</style>
