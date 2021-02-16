<template>
    <suspense>
        <div id="app">
            <Navbar name="Uniforms.edu"/>
            <router-view/>
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
body
{
  font-family: "Open Sans", Arial, sans-serif;
  font-size: 1rem;
  margin: 0;
  padding-top: 150px;
}

#app {
  text-align: center;
}
</style>
