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
    <SentenceGeneration v-if="GenerationTrigger" title="사피엔스" />
  </div>
</template>
<script>
import SentenceGeneration from "./SentenceGeneration.vue";

export default {
  name: "HumanTable",
  props: {},
  components: {
    SentenceGeneration,
  },
  data: function () {
    return {
      GenerationTrigger: false,
      left_items: [
        {
          title: "<strong>사피엔스</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9788934972464.jpg",
          pubDate: "2015.11.24 출시",
          writer: "유발 하라리 외",
          publisher: "김영사",
          userRating: "9.58",
        },
        {
          title: "<strong>소크라테스 익스프레스</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9791190030922.jpg",
          pubDate: "2021.04.28 출시",
          writer: "에릭 와이너 외",
          publisher: "어크로스",
          userRating: "9.59",
        },
      ],
      right_items: [
        {
          title: "<strong>공정하다는 착각</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9791164136452.jpg",
          pubDate: "2020.12.01 출시",
          writer: "마이클 샌델 외",
          publisher: "와이즈베리",
          userRating: "9.38",
        },
        {
          title: "<strong>질서 너머</strong>",
          image: "https://contents.kyobobook.co.kr/sih/fit-in/142x0/pdt/9788901249599.jpg",
          pubDate: "2021.03.22 출시",
          writer: "조던 피터슨 외",
          publisher: "웅진지식하우스",
          userRating: "9.29",
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
