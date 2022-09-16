# kyobobook-review

## frontend

프레임워크: [Vue](https://cli.vuejs.org/)

```
cd frontend
```

frontend 폴더로 이동 후

```
npm install
```

npm 패키지 설치

## backend

프레임워크: [Flask](https://flask.palletsprojects.com/en/2.2.x/)

## Data

[Selenium4](https://www.selenium.dev/)를 활용하여 [교보문고](http://www.kyobobook.co.kr/index.laf)의 2022년 8월 1일부터 2022년 8월 31일까지의 종합 월간 베스트의 각 분야별 책에 대한 리뷰데이터를 구했다.

데이터 진행 사항

- 리뷰 크롤링 ✔️
- 한 페이지 크롤링 ✔️
- 페이지 넘어가는 것 ✔️
- 각 분야의 상위20 책 리뷰 데이터 가져오기 ✔️
- **데이터 용량 문제를 대비하여 최대 60페이지 리뷰만 가져옴** ✔️
- 데이터 크롤링 완료 ✔️
