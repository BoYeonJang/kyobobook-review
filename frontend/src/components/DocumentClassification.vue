<template v-if="trigger">
  <div>
    <div>
      <p class="font-bold underline decoration-indigo-500">오늘은 교양을 쌓고 싶어</p>
      에 어울리는책의 종류는
      <p class="font-bold underline decoration-orange-500">교양과학</p>
      입니다.<br />해당 분야의 베스트 셀러는 다음과 같습니다.
    </div>
    <table class="table-auto">
      <th>교양과학</th>
      <tr>
        <td>코스모스</td>
      </tr>
      <tr>
        <td>이기적 유전자</td>
      </tr>
      <tr>
        <td>엔드 오브 타임</td>
      </tr>
      <tr>
        <td>다정한 것이 살아남는다</td>
      </tr>
      <tr>
        <td>미적분의 쓸모</td>
      </tr>
    </table>
  </div>
</template>

<script>
// import * as API from "../api.js";

export default {
  name: "DocumentClassification",
  props: {
    trigger: Boolean,
  },
  data: function () {
    return {};
  },
  methods: {},
};
</script>
