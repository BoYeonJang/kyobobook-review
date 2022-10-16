# How to Crawling

## Crawling 폴더로 이동

```
cd Crawling
```

## venv 가상환경 실행 방법

### 폴더 진입

```
cd venv/Scripts
```

### 가상환경 실행

```
kyobobook-review/Code/Crawling/venv/Scripts> activate
```

### 가상환경 종료

```
kyobobook-review/Code/Crawling/venv/Scripts> deactivate
```

## pipenv 가상환경 실행 방법

### 가상환경 실행(설치가 되었다는 가정)

```
pipenv shell
```

### 가상환경 확인

```
pipenv --venv
```

### 가상환경 종료

```
exit
```

### 가상환경 삭제

```
pipenv --rm
```

## Crawling 코드 실행

### 교보문고

```
python kyobo-data-crawling.py
```

### 책 한 권만

```
python kyobo-data-crawling-one.py
```

### yes24

```
python yes24_crawling.py
```

### ebook

```
python ebook_crawling.py
```
