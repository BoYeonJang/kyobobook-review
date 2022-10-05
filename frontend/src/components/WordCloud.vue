<template>
  <div>
    <p><b>부자 아빠 가난한 아빠</b>의 키워드입니다.</p>
    <img alt="Word Cloud" src="../assets/wordcloud.png" />
    <img alt="Word Cloud" src="../assets/wordcloud.png" />
  </div>
</template>

<script>
// import * as API from "../api.js";

export default {
  name: "PairClassification",
  props: {},
  data: function () {
    return {};
  },
  methods: {},
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
th,
td {
  border-bottom: 1px solid black;
  border-collapse: collapse;
}
.book_table {
  padding: 20px;
  margin-left: auto;
  margin-right: auto;
}
</style>
