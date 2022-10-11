<template>
  <div>
    <table v-for="item in items" :key="item.title">
      <tr>
        <td rowspan="6"><img v-bind:src="item.image" /></td>
      </tr>
      <tr>
        <td><span v-html="item.title"></span></td>
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
</template>
<script>
export default {
  name: "NovelTable",
  props: {},
  data: function () {
    return {
      items: [
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
};
</script>
<style scoped>
table {
  font-size: 1.25rem;
  text-align: left;
  border: 1px solid #ccc;
}
.float-left {
  float: left;
}
</style>
