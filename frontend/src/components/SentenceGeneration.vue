<template v-if="generationTrigger">
  <div class="font-NotoSans word-cloud-location">
    <div class="word-cloud-card-top">
      <button @click="$emit('close-modal')">&times;</button>
    </div>
    <div class="word-cloud-card-bottom">
      <div>
        <span class="decoration-sky font-bold">{{ title }}</span
        >의 전체적인 워드 클라우드입니다.
      </div>
      <div v-if="title == '코스모스'">
        <img
          alt="Word Cloud"
          src="../assets/WordCloud/코스모스(3차_불용어_사전_반영).png"
          class="word-cloud"
        />
      </div>
      <div v-else-if="title == '사피엔스'">
        <img
          alt="Word Cloud"
          src="../assets/WordCloud/사피엔스(3차_불용어_사전_반영).png"
          class="word-cloud"
        />
      </div>
      <div v-else-if="title == '나미야 잡화점의 기적'">
        <img
          alt="Word Cloud"
          src="../assets/WordCloud/나미야_잡화점의_기적(3차_불용어_사전_반영).png"
          class="word-cloud"
        />
      </div>
    </div>
    <div>
      <span class="decoration-sky font-bold">{{ title }}</span
      >에 대해 더 궁금한 게 있으시다면 입력해주세요.<br />기존 고객 리뷰를 요약해서 알려드립니다.
    </div>
    <!-- search bar -->
    <div class="search-bar">
      <div class="search-svg">
        <svg
          focusable="false"
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 24 24"
          class="search-img"
        >
          <path
            d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"
          ></path>
        </svg>
        <input
          type="text"
          class="generation-search"
          ref="prompt"
          @keypress.enter="api_call"
          name="input"
          placeholder="한줄평에 대해 알 수 있어요."
        />
      </div>
    </div>
    <div>
      <span class="font-bold">한줄평</span>
      <br />
      <span ref="generation" id="generation" class="mb-0"></span>
    </div>
    <!-- post 테스트용 로그인 -->
    <!-- <div>
      <input class="input_box" type="text" v-model="id" />
      <input class="input_box" type="password" v-model="password" />
      <button id="loginBtn" @click="loginHandler">로그인</button>
    </div> -->
    <!-- post 테스트용 -->
  </div>
</template>

<script>
import * as API from "../api.js";

export default {
  name: "SentenceGeneration",
  props: {
    title: String,
  },
  data: function () {
    return {
      // testVal: "",
      // trigger: false,
      // 문장 생성 data
      prompt: "",
      min_length: 20,
      max_length: 30,
      top_p: 0.8,
      top_k: 30,
      repetition_penalty: 1.5,
      no_repeat_ngram_size: 3,
      temperature: 0.9,
      generationTrigger: false,
    };
  },
  methods: {
    async api_call() {
      console.log("this: ", this);
      const input = {
        prompt: this.$refs.prompt.value,
        min_length: this.min_length,
        max_length: this.max_length,
        top_p: this.top_p,
        top_k: this.top_k,
        repetition_penalty: this.repetition_penalty,
        no_repeat_ngram_size: this.no_repeat_ngram_size,
        temperature: this.temperature,
      };
      console.log(input);
      await API.post("api", { ...input })
        .then(res => res.json())
        .then(body => {
          // const reader = body.getReader();
          console.log("body: ", body);
          console.log("this.$refs.generation: ", this.$refs.generation);
          this.$refs.generation.innerText = body["result"];
          this.generationTrigger = true;
        })
        .catch(err => console.error("실패했습니다.", err));
    },
    // get 테스트
    // async api_call() {
    //   await API.get("api")
    //     .then(res => res.json())
    //     .then(data => console.log(data))
    //     .catch(err => console.log(err));
    // },

    // post 테스트용
    // async loginHandler() {
    //   if (this.id && this.password) {
    //     alert("ID : " + this.id + "\nPassword : " + this.password);
    //     await API.post("predict", { id: this.id, pass: this.password })
    //       .then(res => res.json())
    //       .then(data => {
    //         console.log(data);
    //         console.log("아이디: ", this.id);
    //         console.log("비밀번호: ", this.password);
    //         this.testVal = data.data.id;
    //         this.trigger = true;
    //       })
    //       .catch(err => console.error(err));
    //   } else {
    //     alert("아이디나 비밀번호를 확인하세요.");
    //   }
    // },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.font-NotoSans {
  font-family: "Noto Sans KR", sans-serif;
}
.word-cloud {
  width: 30rem;
  margin: 2rem;
}
.decoration-sky {
  text-decoration-line: underline;
  text-decoration-color: #0ea5e9;
}
.font-bold {
  font-weight: 700;
}
/* 검색바 style 여기 시작 */
.search-bar {
  border: 0px solid;
  width: fit-content;
  border-radius: 1rem;
  display: inline-block;
  margin: 3rem;
  background: white;
  box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
}
.search-svg {
  display: flex;
}
.search-img {
  width: 1.7rem;
  padding: 0 0.5rem 0 0.5rem;
}
.generation-search {
  padding: 1rem 1rem 1rem 0px;
  border-radius: 1rem;
  width: 30rem;
  font-size: 1rem;
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
/* 검색바 style 여기 까지 */
/* 워드 클라우드 카드 여기 시작 */
/* .word-cloud-card {
  border: 0px solid;
  border-radius: 1rem;
  padding: 1rem;
  margin: 3rem 0 3rem 0;
  width: 65rem;
  box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  background-color: rgb(244, 244, 244);
  display: inline-block;
} */
.word-cloud-card-top {
  border: 0px solid;
  border-top-left-radius: 0.5rem;
  border-top-right-radius: 0.5rem;
  padding: 1rem;
  margin: 3rem 0 0 0;
  width: 65rem;
  box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  background-color: rgb(244, 244, 244);
  display: inline-block;
  text-align: right;
}
.word-cloud-card-bottom {
  border: 0px solid;
  border-bottom-right-radius: 0.5rem;
  border-bottom-left-radius: 0.5rem;
  padding: 1rem;
  margin: 0 0 3rem 0;
  width: 65rem;
  box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  background-color: rgb(244, 244, 244);
  display: inline-block;
}
/* 워드 클라우드 카드 여기 까지 */
button {
  border: 0;
  outline: 0;
  cursor: pointer;
  font-size: 2rem;
  background-color: rgb(244, 244, 244);
}
.word-cloud-location {
  position: relative;
  bottom: 31.5rem;
}
</style>
