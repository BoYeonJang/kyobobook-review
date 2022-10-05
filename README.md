# kyobobook-review

## frontend

프레임워크: [Vue](https://cli.vuejs.org/)

로컬 실행 방법

```
cd frontend
```

```
npm install
```

```
npm run serve
```

> `http://localhost:8080/`

## backend

프레임워크: [Flask](https://flask.palletsprojects.com/en/2.2.x/)

로컬 실행 방법

```
pipenv install && pipenv shell
```

```
cd backend
```

```
flask run
```

> `http://localhost:5000/`

## docker

팀 프로젝트로 팀원 및 서버와 개발 환경을 쉽게 동기화하기 위해 [Docker](https://www.docker.com/)를 사용했다.

`kyobobook-review`가 있는 폴더로 진입 후

```
docker-compose up
```

`frontend:80`, `backend:7000`이 실행된다.

## 폴더 구조

```
├── backend/
│   ├── app.ini
│   ├── app.py
│   ├── wsgi.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── ...
│   ├── src/
│   │   ├── components/
│   │   └── App.vue
│   ├── api.js
│   ├── nginx.conf
│   └── Dockerfile
├── Code/
│   ├── Analysis/
│   └── Crawling/
├── Data/
│   ├── 리뷰순/
│   ├── 모델/
│   │   └── model.pt
│   ├── 분야별/
│   └── Top3/
├── nlpbook/
│   ├── checkpoint-doccls/
│   └── epoch=0-val_loss=0.43.ckpt
├── docker-compose.yml
├── Pipfile
└── README.md
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

---

용량 문제로 인해 최소 기능 동작을 위해 리뷰가 가장 많은 책 Top3를 선정했다.

1. 나미야 잡화점의 기적 - 소설
2. 코스모스 - 교양과학
3. 사피엔스 - 인문

교보문고 + 교보ebook + yes24의 데이터를 크롤링했다.

|     | 나미야 잡화점의 기적 | 코스모스 | 사피엔스 |
| --- | -------------------- | -------- | -------- |
| row | 3610                 | 1898     | 2137     |

## pipenv 설정

Pipenv 설치

```
pip3 install pipenv
또는
pip install pipenv
```

clone한 레포지토리 폴더로 이동 후 가상환경 패키지 설치

```
pipenv install
```

실행

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
