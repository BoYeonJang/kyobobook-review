# python의 3.10.5의 버전을 사용한다.
FROM python:3.10.5 
# 루트디렉터리(/)에 app 디렉터리를 만든다.
RUN mkdir /backend
# flask 디렉터리안에 있는 python의 dependency를 설치 할 리스트를 적어둔 것이다.
COPY requirements.txt /
# COPY 한 dependecy 를 설치하고,
RUN pip3 install -r /requirements.txt
# 현재 있는 디렉토리(flask) 내부에 있는 모든 파일들을 /backend에 복사하는 명령어이다.
COPY . /backend
# 해당 디렉터리에서 모든 것을 실행한다
WORKDIR /backend

CMD ["gunicorn", "app.ini"]