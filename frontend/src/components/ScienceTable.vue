<template>
  <div>
    <div class="inline-flex mt-12 table_card">
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
    <SentenceGeneration v-if="GenerationTrigger" title="코스모스" />
  </div>
</template>
<script>
import SentenceGeneration from "./SentenceGeneration.vue";

export default {
  name: "ScienceTable",
  props: {},
  components: {
    SentenceGeneration,
  },
  data: function () {
    return {
      GenerationTrigger: false,
      left_items: [
        {
          title: "<strong>코스모스</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9788983711892.jpg",
          pubDate: "2010.01.20 출시",
          writer: "칼 세이건 외",
          publisher: "사이언스북스",
          userRating: "9.66",
        },
        {
          title: "<strong>이기적 유전자(40주년 기념판)</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9788932473901.jpg",
          pubDate: "2018.10.20 출시",
          writer: "리처드 도킨스 외",
          publisher: "을유문화사",
          userRating: "9.52",
        },
      ],
      right_items: [
        {
          title: "<strong>엔드 오브 타임</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9791164137411.jpg",
          pubDate: "2021.02.15 출시",
          writer: "브라이언 그린 외",
          publisher: "와이즈베리",
          userRating: "9.69",
        },
        {
          title: "<strong>다정한 것이 살아남는다</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9791197413025.jpg",
          pubDate: "2021.07.26 출시",
          writer: "브라이언 헤어 외",
          publisher: "디플롯",
          userRating: "9.64",
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
.table_card {
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
