<template>
  <div>
    <div class="input-group mb-3">
      <input
        type="text"
        class="review_search"
        aria-describedby="basic-addon3"
        ref="prompt"
        id="prompt"
        v-model="sentence_generation_data"
        @keypress.enter="api_call"
        name="input"
        placeholder="프롬프트를 입력하세요"
      />
    </div>
    <!-- <p class="card-text"> -->
    <div class="alert alert-info" role="alert">
      <b>생성 결과</b>
      <p ref="generation" id="generation" v-bind="result_generation" class="mb-0"></p>
    </div>
    <!-- </p> -->
    <!-- post 테스트용 -->
    <div>
      <input class="input_box" type="text" v-model="id" />
      <input class="input_box" type="password" v-model="password" />
      <button id="loginBtn" @click="loginHandler">로그인</button>
    </div>
    <!-- post 테스트용 -->
  </div>
</template>

<script>
import * as API from "../api.js";

export default {
  name: "SentenceGeneration",
  props: {},
  data: function () {
    return {
      sentence_generation_data: "",
      result_generation: "",
      testVal: "",
      trigger: false,
    };
  },
  methods: {
    async api_call() {
      // const sentence = this.$refs.prompt;
      const sentence = this.sentence_generation_data;
      // const input = { prompt: sentence };
      console.log(sentence);
      await API.post("api", { gener: this.sentence_generation_data })
        .then(res => res.json())
        .then(data => {
          console.log("data: ", data);
          this.result_generation = data.data.retult;
        });
    },
    // post 테스트용
    async loginHandler() {
      if (this.id && this.password) {
        alert("ID : " + this.id + "\nPassword : " + this.password);
        await API.post("predict", { id: this.id, pass: this.password })
          .then(res => res.json())
          .then(data => {
            console.log(data);
            console.log("아이디: ", this.id);
            console.log("비밀번호: ", this.password);
            this.testVal = data.data.id;
            this.trigger = true;
          })
          .catch(err => console.error(err));
      } else {
        alert("아이디나 비밀번호를 확인하세요.");
      }
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.review_search {
  /* margin: 20px; */
  padding: 15px;
  border: 1px solid black;
  border-radius: 5px;
  width: 40rem;
  font-size: 15px;
}
</style>
