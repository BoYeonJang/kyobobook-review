<template>
  <div class="font-IBM downUp">
    <!-- main -->
    <div class="font-Myung hello">
      <div class="mt-13">
        <span>안녕하세요.</span>
      </div>
      <div class="mt-2">
        <span>오늘은 어떤 책을 읽고 싶은지 </span>
        <span class="decoration-orange font-bold">당신의 생각</span>을 적어주세요.
      </div>
    </div>
    <!-- search bar -->
    <div class="search_bar">
      <div class="search_svg">
        <svg
          focusable="false"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          class="search_img"
        >
          <path
            d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"
          ></path>
        </svg>
        <input
          type="text"
          class="think_search"
          ref="prompt"
          @keypress.enter="api_call"
          name="input"
          placeholder="당신의 생각을 적어주세요."
        />
      </div>
    </div>
    <!-- table -->
    <div v-if="ClassificationTrigger" class="text-xl">
      <span class="decoration-indigo font-bold">{{ this.sentence }}</span
      >에 어울리는 분야는 <span class="decoration-indigo font-bold">{{ this.prediction }}</span
      >입니다.
      <br />
      <span class="">해당 분야의 베스트 셀러는 다음과 같습니다.</span>
      <div v-if="this.prediction == '과학'">
        <ScienceTable />
      </div>
      <div v-else-if="this.prediction == '인문'">
        <HumanTable />
      </div>
      <div v-else-if="this.prediction == '소설'">
        <NovelTable />
      </div>
      <!-- <SentenceGeneration /> -->
    </div>
  </div>
</template>

<script>
// import SentenceGeneration from "./SentenceGeneration.vue";
import ScienceTable from "./ScienceTable.vue";
import HumanTable from "./HumanTable.vue";
import NovelTable from "./NovelTable.vue";
import * as API from "../api.js";

export default {
  name: "HelloWorld",
  props: {},
  components: {
    // SentenceGeneration,
    ScienceTable,
    HumanTable,
    NovelTable,
  },
  data: function () {
    return {
      prompt: "",
      prediction: "",
      sentence: "",
      ClassificationTrigger: false,
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
          // this.$refs.prediction = body["prediction"];
          // this.$refs.sentence = body["sentence"];
          this.prediction = body["prediction"];
          this.sentence = body["sentence"];
          this.ClassificationTrigger = true;
        })
        .catch(err => console.error("실패했습니다.", err));
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.font-Myung {
  font-family: "Song Myung", serif;
}
.font-IBM {
  font-family: "IBM Plex Sans KR", sans-serif;
}
/* 아래에서 위로 애니메이션 여기 시작 */
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translate3d(0, 100%, 0);
  }
  to {
    opacity: 1;
    transform: translateZ(0);
  }
}
.downUp {
  position: relative;
  animation: fadeInUp 1s;
}
/* 아래에서 위로 애니메이션 여기 까지 */
.hello {
  font-size: 3.5rem;
  text-align: center;
}
.decoration-orange {
  text-decoration-line: underline;
  text-decoration-color: #f97316;
}
.decoration-indigo {
  text-decoration-line: underline;
  text-decoration-color: #6366f1;
}
.search_bar {
  border: solid;
  width: fit-content;
  border-radius: 1rem;
  display: inline-block;
  margin: 3rem;
  background: white;
}
.search_svg {
  display: flex;
}
.think_search {
  padding: 1rem 1rem 1rem 0px;
  border-radius: 1rem;
  width: 30rem;
  font-size: 1rem;
  box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  border-width: 0px;
}
input:focus {
  outline: none;
}
input::placeholder {
  opacity: 0.5;
  font-style: italic;
  font-weight: 700;
}
.mt-2 {
  margin-top: 2rem;
}
.mt-13 {
  margin-top: 13rem;
}
.font-bold {
  font-weight: 700;
}
.text-xl {
  font-size: 1.25rem;
}
.search_img {
  width: 1.7rem;
  padding: 0 0.5rem 0 0.5rem;
}
</style>
