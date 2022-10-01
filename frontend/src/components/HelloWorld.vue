<template>
  <div class="hello">
    <h1>안녕하세요.<br />오늘은 어떤 책을 읽고 싶은지 생각을 적어주세요.</h1>
    <input class="main_search" />
    <p><b>오늘은 교훈이 있는 책을 읽고 싶어</b>에 어울리는책의 종류는 <b>경제경영</b>입니다.<br /><b>경제경영</b> 분야의 베스트 셀러는 다음과 같습니다.</p>
    <table class="book_table">
      <th>경제경영</th>
      <tr>
        <td>부자 아빠 가난한 아빠</td>
      </tr>
      <tr>
        <td>우리는 어디서 살아야 하는가</td>
      </tr>
      <tr>
        <td>부자의 그릇</td>
      </tr>
      <tr>
        <td>인천 부동산의 미래</td>
      </tr>
      <tr>
        <td>변화하는 세계 질서</td>
      </tr>
    </table>
    <p><b>부자 아빠 가난한 아빠</b>의 키워드입니다.</p>
    <img alt="Word Cloud" src="../assets/wordcloud.png" />
    <img alt="Word Cloud" src="../assets/wordcloud.png" />
    <p><b>부자 아빠 가난한 아빠</b>에 대해 더 궁금한 게 있으시다면 입력해주세요.<br />기존 고객 리뷰를 요약해서 알려드립니다.</p>
    <input class="review_search" />
    <SentenceGeneration />
  </div>
</template>

<script>
import SentenceGeneration from "./SentenceGeneration.vue";

export default {
  name: "HelloWorld",
  props: {},
  components: {
    SentenceGeneration,
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.main_search {
  margin: 20px;
  padding: 15px;
  border: 1px solid black;
  border-radius: 5px;
  width: 40rem;
  font-size: 15px;
}
.review_search {
  /* margin: 20px; */
  padding: 15px;
  border: 1px solid black;
  border-radius: 5px;
  width: 40rem;
  font-size: 15px;
}
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
p {
  padding: 20px;
}
</style>
