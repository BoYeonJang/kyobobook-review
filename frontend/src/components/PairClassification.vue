<template>
  <div>
    <p>
      <b>오늘은 교양을 쌓고 싶어</b>에 어울리는책의 종류는 <b>교양과학</b>입니다.<br /><b
        >교양과학</b
      >
      분야의 베스트 셀러는 다음과 같습니다.
    </p>
    <table class="book_table">
      <th>교양과학</th>
      <tr>
        <td>코스모스</td>
      </tr>
      <tr>
        <td>이기적 유전자</td>
      </tr>
      <tr>
        <td>엔드 오브 타임</td>
      </tr>
      <tr>
        <td>다정한 것이 살아남는다</td>
      </tr>
      <tr>
        <td>미적분의 쓸모</td>
      </tr>
    </table>
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
