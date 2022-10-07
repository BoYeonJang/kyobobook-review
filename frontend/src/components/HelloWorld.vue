<template>
  <div class="hello">
    <h1>안녕하세요.<br />오늘은 어떤 책을 읽고 싶은지 생각을 적어주세요.</h1>
    <input
      type="text"
      class="review_search"
      aria-describedby="basic-addon3"
      ref="prompt"
      @keypress.enter="api_call"
      name="input"
      placeholder="프롬프트를 입력하세요"
    />
    <div class="alert alert-info" role="alert">
      <h5 ref="prediction" class="alert-heading"></h5>
      <!-- <p ref="sentence" class="mb-0"></p> -->
    </div>
    <DocumentClassification />
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
import * as API from "../api.js";

export default {
  name: "HelloWorld",
  props: {},
  components: {
    DocumentClassification,
    SentenceGeneration,
  },
  data: function () {
    return {
      prompt: "",
      prediction: "",
      // sentence: "",
    };
  },
  methods: {
    async api_call() {
      console.log("this: ", this);
      const input = {
        prompt: this.$refs.prompt.value,
      };
      console.log(input);
      await API.post("classification", { ...input })
        .then(res => res.json())
        .then(body => {
          console.log("body: ", body);
          // console.log("this.$refs.generation: ", this.$refs.generation);
          this.$refs.prompt.innerText = body["result"];
          this.$refs.prediction.innerText = body["prediction"];
          // this.$refs.sentence.innerText = body["sentence"];
        })
        .catch(err => console.error("실패했습니다.", err));
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
