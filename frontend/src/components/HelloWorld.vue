<template>
  <div class="hello p-40">
    <p class="text-5xl font-bold drop-shadow-xl">안녕하세요.</p>
    <p class="text-5xl font-bold drop-shadow-xl">
      오늘은 어떤 책을 읽고 싶은지
      <span class="font-bold underline decoration-orange-500">당신의 생각</span>을 적어주세요.
    </p>
    <div class="text-center pl-96">
      <label
        for="default-search"
        class="mb-2 text-sm font-medium text-gray-900 sr-only dark:text-gray-300"
        >Search</label
      >
      <div class="relative mt-10 content-center">
        <div class="flex absolute inset-y-0 left-0 items-center pl-3 pointer-events-none">
          <svg
            aria-hidden="true"
            class="w-5 h-5 text-gray-500 dark:text-gray-400"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            ></path>
          </svg>
        </div>
        <input
          type="text"
          aria-describedby="basic-addon3"
          class="block p-4 pl-10 w-96 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          ref="prompt"
          @keypress.enter="api_call"
          name="input"
          placeholder="당신의 생각을 적어주세요."
          required
        />
      </div>
    </div>
    <!-- 예전 input 태그 -->
    <!-- <div>
      <input
        type="text"
        class="m-5 p-4 text-2xl w-96 rounded-lg"
        aria-describedby="basic-addon3"
        ref="prompt"
        @keypress.enter="api_call"
        name="input"
        placeholder="당신의 생각을 적어주세요."
      />
    </div> -->
    <div v-if="trigger">
      <p>
        <span ref="prediction" class="alert-heading"></span>에 어울리는 책의 종류는
        <span ref="sentence" class="mb-0"></span>입니다.
        <br />
        해당 분야의 베스트 셀러는 다음과 같습니다.
      </p>
      <div>
        <p>
          <b>부자 아빠 가난한 아빠</b>에 대해 더 궁금한 게 있으시다면 입력해주세요.<br />기존 고객
          리뷰를 요약해서 알려드립니다.
        </p>
      </div>
      <SentenceGeneration />
    </div>
    <!-- <DocumentClassification :trigger="trigger" /> -->
  </div>
</template>

<script>
// import DocumentClassification from "./DocumentClassification";
import SentenceGeneration from "./SentenceGeneration.vue";
import * as API from "../api.js";

export default {
  name: "HelloWorld",
  props: {},
  components: {
    // DocumentClassification,
    SentenceGeneration,
  },
  data: function () {
    return {
      prompt: "",
      prediction: "",
      sentence: "",
      trigger: false,
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
          this.$refs.prediction = body["prediction"];
          this.$refs.sentence = body["sentence"];
          this.trigger = true;
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
p {
  padding: 20px;
}
</style>
