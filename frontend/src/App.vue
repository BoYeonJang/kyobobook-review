<template>
  <div>
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
body {
  background: linear-gradient(to right, #2af598, #009efd);
  width: 100%;
  height: 100%;
}
#app {
  text-align: center;
}
</style>
