<template>
  <div class="hello">
    <h1>안녕하세요.<br />오늘은 어떤 책을 읽고 싶은지 생각을 적어주세요.</h1>
    <input class="main_search" @keypress.enter="pairHandler" />
    <DocumentClassification v-show="pairShow" />
    <p>
      <b>부자 아빠 가난한 아빠</b>에 대해 더 궁금한 게 있으시다면 입력해주세요.<br />기존 고객
      리뷰를 요약해서 알려드립니다.
    </p>
    <SentenceGeneration />
  </div>
</template>

<script>
import DocumentClassification from "./DocumentClassification";
import SentenceGeneration from "./SentenceGeneration.vue";

export default {
  name: "HelloWorld",
  props: {},
  components: {
    DocumentClassification,
    SentenceGeneration,
  },
  data: function () {
    return { pairShow: false };
  },
  methods: {
    pairHandler() {
      this.pairShow = !this.pairShow;
    },
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
