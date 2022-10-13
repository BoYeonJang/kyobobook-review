<template>
  <div>
    <!-- logo -->
    <div class="logo">
      <span class="font-bold text-xl">A<span class="signature-color">i</span>Letter</span>
    </div>
  </div>
</template>

<script>
export default {
  name: "LogoBar",
  props: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.logo {
  text-align: left;
  margin: 2rem 0 0 2rem;
}
.signature-color {
  color: rgb(146, 208, 80);
}
.font-bold {
  font-weight: 700;
}
.text-xl {
  font-size: 1.25rem;
}
</style>
