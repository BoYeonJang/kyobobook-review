<template>
  <div>
    <div class="table-card">
      <!-- table 좌측 -->
      <div class="float-left mr-20">
        <table v-for="item in left_items" :key="item.title">
          <tr>
            <td rowspan="6"><img v-bind:src="item.image" /></td>
          </tr>
          <tr>
            <a>
              <td><span v-html="item.title" @click="ClickWord"></span></td>
            </a>
          </tr>
          <tr>
            <td><span v-html="item.pubDate"></span></td>
          </tr>
          <tr>
            <td><span v-html="item.writer"></span></td>
          </tr>
          <tr>
            <td><span v-html="item.publisher"></span></td>
          </tr>
          <tr>
            <td><span v-html="item.userRating"></span></td>
          </tr>
        </table>
      </div>
      <!-- table 우측 -->
      <div>
        <table v-for="item in right_items" :key="item.title">
          <tr>
            <td rowspan="6"><img v-bind:src="item.image" /></td>
          </tr>
          <tr>
            <a>
              <td><span v-html="item.title" @click="ClickWord"></span></td>
            </a>
          </tr>
          <tr>
            <td><span v-html="item.pubDate"></span></td>
          </tr>
          <tr>
            <td><span v-html="item.writer"></span></td>
          </tr>
          <tr>
            <td><span v-html="item.publisher"></span></td>
          </tr>
          <tr>
            <td><span v-html="item.userRating"></span></td>
          </tr>
        </table>
      </div>
    </div>
    <SentenceGeneration v-if="GenerationTrigger" title="나미야 잡화점의 기적" />
  </div>
</template>
<script>
import SentenceGeneration from "./SentenceGeneration.vue";

export default {
  name: "NovelTable",
  props: {},
  components: {
    SentenceGeneration,
  },
  data: function () {
    return {
      GenerationTrigger: false,
      left_items: [
        {
          title: "<strong>나미야 잡화점의 기적</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9788972756194.jpg",
          pubDate: "2012.12.19 출시",
          writer: "히가시노 게이고 외",
          publisher: "현대문학",
          userRating: "9.5",
        },
        {
          title: "<strong>달러구트 꿈 백화점(레인보우 에디션)</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9791165341909.jpg",
          pubDate: "2020.07.08 출시",
          writer: "이미예",
          publisher: "팩토리나인",
          userRating: "9.45",
        },
      ],
      right_items: [
        {
          title: "<strong>미드나잇 라이브러리(1주년 스페셜 에디션)</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9791191056556.jpg",
          pubDate: "2021.04.28 출시",
          writer: "매트 헤이그 외",
          publisher: "인플루엔셜",
          userRating: "9.46",
        },
        {
          title: "<strong>달러구트 꿈 백화점 2(레인보우 에디션)</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9791165343729.jpg",
          pubDate: "2021.07.27 출시",
          writer: "이미예",
          publisher: "팩토리나인",
          userRating: "9.77",
        },
      ],
    };
  },
  methods: {
    async ClickWord() {
      this.GenerationTrigger = true;
    },
  },
};
</script>
<style scoped>
table {
  font-size: 1.25rem;
  text-align: left;
}
a:hover {
  text-decoration: underline;
  cursor: pointer;
}
img {
  width: 7rem;
  height: 11rem;
  padding-right: 1rem;
}
.table-card {
  display: inline-flex;
  border: 0px solid;
  border-radius: 1rem;
  padding: 1rem;
  margin: 3rem 0 3rem 0;
  box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25);
  background-color: rgba(255, 255, 255, 0.5);
}
.float-left {
  float: left;
}
.mr-20 {
  margin-right: 5rem;
}
</style>
