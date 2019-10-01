# 뚞딲뚞딲 플라스크 스타터팩
이정윤이 귀찮아서 만든 ddoddak-Flask

## 구축편

#### Git
```buildoutcfg
1. git을 설치한다.
    $ sudo apt install git
    
2. git에서 뚞딲뚞딲 플라스크를 받아온다.
    $ git clone https://github.com/agurimon/ddoddak-flask
```

#### Python
```buildoutcfg
1. python3, python3-pip을 설치한다.
    $ sudo apt install python3 python3-pip
```

#### Mysql
```buildoutcfg
1. 컴퓨터에 mysql을 설치한다.
    $ sudo apt install mysql-server
    
    (error) 만약 에러가 난다?
        $ sudo apt install libmysqlclient-dev build-essential libssl-dev libffi-dev 
   ```

#### Virtualenv
```buildoutcfg
1. virtualenv 설치한다.
    $ sudo apt install virtualenv
    
    (error) 만약 에러가 난다?
        $ sudo apt-get install letsencrypt
        $ export LC_ALL="en_US.UTF-8"
        $ export LC_CTYPE="en_US.UTF-8"

2. 프로젝트에 venv(가상환경)을 만든다.
    $ virtualenv venv -p python3

3. venv을 활성화한다.
    $ source ./venv/bin/activate
```

#### 라이브러리 설치
```buildoutcfg
1. 라이브러리를 설치한다.
     $ pip install -r requirements.txt
```

#### bower 설치
```buildoutcfg
1. nodejs와 npm 설치
    $ sudo apt install nodejs npm

2. node와 nodejs 연결
    $ ln -s /usr/bin/nodejs /usr/local/bin/node
    
3. bower(웹 프론트엔드 패키지 관리자) 설치
    $ sudo npm install -g bower

4. bower 라이브러리 설치
     $ bower install
```

## 실행편
```buildoutcfg
1. venv을 활성화한다.
     $ source ./venv/bin/activate

2.
     $ source .env  (.env안에 (1)이 포함되어 있음)

3-1. 실행한다.
     $ flask run

3-2. 포트번호를 바꾸고 싶다.
    - runserver.py에서 바꾼다.
     $ python runserver.py
```

## Apache
```buildoutcfg
1. Apache (httpd) 설치 - 내 웹서버를 전세계에 뿌려줄 모듈
2. Flask 설치
3. mod_wsgi 설치 - Apache와 Flask를 연결 시켜줄 모듈
4. 연결 작업
5. 확인
pip install -v mod_wsgi-httpd
pip install mod_wsgi
mod_wsgi-express start-server
```

## 오류
```buildoutcfg

```
