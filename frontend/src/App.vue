<template>
  <div
    class="font-IBM text-center text-black bg-gradient-to-r from-[#6ADE64] to-[#36777C] w-screen h-full"
  >
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
}
</style>
