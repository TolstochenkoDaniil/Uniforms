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
  margin: 0em;
  padding: 0em;
}

#app {
  text-align: center;
  margin-top: 8em;
  box-sizing: border-box;
}
</style>
