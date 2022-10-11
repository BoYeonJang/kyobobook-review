<template>
  <div class="app">
    <HelloWorld />
  </div>
</template>

<script>
import HelloWorld from "./components/HelloWorld.vue";
import "./style.css";

export default {
  name: "App",
  components: {
    HelloWorld,
  },
};
</script>
<style>
#app {
  text-align: center;
}
</style>
