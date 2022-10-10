<template v-if="generationTrigger">
  <div>
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
          class="block p-4 pl-10 w-96 text-sm text-gray-900 bg-gray-50 rounded-lg border border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
          aria-describedby="basic-addon3"
          ref="prompt"
          id="prompt"
          @keypress.enter="api_call"
          name="input"
          placeholder="프롬프트를 입력하세요"
        />
      </div>
    </div>
    <div class="alert alert-info" role="alert">
      <b>생성 결과</b>
      <p ref="generation" id="generation" class="mb-0"></p>
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
  props: {},
  data: function () {
    return {
      // testVal: "",
      // trigger: false,
      // 여기서부터
      prompt: "",
      min_length: 10,
      max_length: 30,
      top_p: 1.0,
      top_k: 1,
      repetition_penalty: 1.0,
      no_repeat_ngram_size: 0,
      temperature: 1.0,
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
<style scoped></style>
