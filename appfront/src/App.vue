<template>
  <div id="app">
    <IndexMain></IndexMain>
  </div>
</template>

<script>
import IndexMain from './components/IndexMain'

export default {
  name: 'app',
  components: {
    IndexMain
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
