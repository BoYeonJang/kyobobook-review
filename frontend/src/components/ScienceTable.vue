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
  name: "ScienceTable",
  props: {},
  data: function () {
    return {
      items: [
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
