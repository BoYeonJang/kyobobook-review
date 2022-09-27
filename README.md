# kyobobook-review

## frontend

프레임워크: [Vue](https://cli.vuejs.org/)

## backend

프레임워크: [Flask](https://flask.palletsprojects.com/en/2.2.x/)

```
flask --debug run
```

## Data

[Selenium4](https://www.selenium.dev/)를 활용하여 [교보문고](http://www.kyobobook.co.kr/index.laf)의 2022년 8월 1일부터 2022년 8월 31일까지의 종합 월간 베스트의 각 분야별 책에 대한 리뷰데이터를 구했다.

데이터 진행 사항

- 리뷰 크롤링 ✔️
- 한 페이지 크롤링 ✔️
- 페이지 넘어가는 것 ✔️
- 각 분야의 상위20 책 리뷰 데이터 가져오기 ✔️
- **데이터 용량 문제를 대비하여 최대 60페이지 리뷰만 가져옴** ✔️
- 데이터 크롤링 완료 ✔️

## pipenv 설정

Pipenv 설치

```
pip3 install pipenv
또는
pip install pipenv
```

clone한 레포지토리 폴더로 이동 후

```
pipenv shell
```

가상환경에 제대로 동작하는지 확인 하려면

```
pipenv --venv
```

가상환경 종료는

```
exit
```

가상환경 삭제는

```
pipenv --rm
```

## 크롤링 방법

`{kyobo-data-crawling}.py`가 위치한 폴더로 이동 후

```
python kyobo-data-crawling.py
```

책 한 권만 이라면

```
python kyobo-data-crawling-one.py
```

## 서비스 아키텍처

![서비스_아키텍처](./img/서비스_아키텍처.png)
