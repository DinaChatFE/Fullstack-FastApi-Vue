<template>
  <notifications position="top right" classes="my-custom-class">
      <p>well</p>
  </notifications>
  <router-view />
</template>

<script>
export default {
  name: "App",
};
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Crimson+Pro:wght@200&display=swap");
#app {
  font-family: "Crimson Pro", serif;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background-color: #f5f6f7;
}

</style>