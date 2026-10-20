# Flask 간단 은행 웹 애플리케이션

Flask로 만든 간단한 은행 웹앱입니다. **로그인, 입금, 출금, 잔액 조회** 기능이 있습니다.
데이터베이스 대신 텍스트 파일(`bank.txt`)에 사용자 정보와 잔액을 저장합니다.

## 데이터

`project_bank/bank.txt`에 한 줄에 한 명씩 사용자 정보가 저장됩니다.

```text
아이디,비밀번호,잔액
```

파일이 없으면 기본 사용자(`admin`)로 자동 생성됩니다.

## 소스 구성

```text
project_bank/
└── project_bank/
    ├── app.py              # Flask 서버(라우팅, 파일 입출력)
    ├── bank.txt            # 사용자 데이터 파일
    └── templates/
        ├── login.html      # 로그인 화면
        └── main.html       # 잔액·입출금 화면
```

## 기능

| 경로 | 기능 |
| --- | --- |
| `/` | 홈 화면(로그인 링크) |
| `/login` | 아이디와 비밀번호로 로그인, 성공하면 잔액 화면으로 이동 |
| `/input` | 입금: 잔액을 늘리고 파일에 저장 |
| `/output` | 출금: 잔액을 줄이고 파일에 저장 |

## 실행 방법

```bash
pip install flask
cd project_bank
python app.py
```

브라우저에서 `http://127.0.0.1:5000`에 접속합니다.
