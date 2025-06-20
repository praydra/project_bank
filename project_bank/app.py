from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATA_FILE = "bank.txt" #DB 대용, 사용자 데이터 생성

# 데이터 초기화 (파일이 없으면 생성)
def init_data():
    try:
        with open(DATA_FILE, "r") as f:
            pass
    except FileNotFoundError:
        with open(DATA_FILE, "w") as f:
            f.write("admin,1234,1000.0")  # 기본 사용자자 파일 생성

init_data()

# 파일에서 사용자 데이터 읽기
def read_data():
    users = {}
    with open(DATA_FILE, "r") as f:
        for line in f:
            username, password, balance = line.strip().split(",")
            users[username] = {"password": password, "balance": float(balance)}
    return users

# 파일에 사용자 데이터 쓰기
def write_data(users):
    with open(DATA_FILE, "w") as f:
        for username, info in users.items():
            f.write(f"{username},{info['password']},{info['balance']}\n")

@app.route('/')
def home():
    return "<h2>홈페이지 - <a href='/login'>로그인</a></h2>"

# 사용자 로그인
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['username']
        user_pw = request.form['password']

        users = read_data()
        # if문을 이용한 로그인 검증
        if user_id in users and user_pw == users[user_id]["password"]:
            return render_template('main.html', user_id=user_id, welcomusesr=f"안녕하세요, {user_id}님!", balance=users[user_id]["balance"])
        else:
            # 실패했을 경우 다시 로그인 페이지로, 에러 메시지 포함
            return render_template('login.html', error="아이디 또는 비밀번호가 틀렸습니다.")

    return render_template('login.html')

# 입금
@app.route('/input', methods=['GET', 'POST'])
def input():
    if request.method == 'POST':
        user_id = request.form['user_id']
        money = float(request.form['money'])

        users = read_data()
        # id 값으로 금액을 가져온 후 잔액을 추가한다.
        if user_id in users:
            amount = float(users[user_id]["balance"])
            amount += money

            users[user_id]["balance"] = amount
            write_data(users)
            return render_template('main.html', user_id=user_id, welcomusesr=f"안녕하세요, {user_id}님!", balance=users[user_id]["balance"], message=f"{money}원 입금처리되었습니다." )
        else:
            # 실패했을 경우 다시 로그인 페이지로, 에러 메시지 포함
            return render_template('login.html', error="아이디를 찾지 못했습니다.")

    return render_template('login.html')

# 출금
@app.route('/output', methods=['GET', 'POST'])
def output():
    if request.method == 'POST':
        user_id = request.form['user_id']
        money = float(request.form['money'])

        users = read_data()
        # id 값으로 금액을 가져온 후 잔액에에 추가한다.
        if user_id in users:
            amount = float(users[user_id]["balance"])

            if amount - money < 0:
                return render_template('main.html', user_id=user_id, welcomusesr=f"안녕하세요, {user_id}님!", balance=users[user_id]["balance"], error="잔액이 -가 될 수 없습니다.")
            else:
                amount -= money
                users[user_id]["balance"] = amount
                write_data(users)
                return render_template('main.html', user_id=user_id, welcomusesr=f"안녕하세요, {user_id}님!", balance=users[user_id]["balance"], message=f"{money}원 출금처리되었습니다.")
        else:
            # 실패했을 경우 다시 로그인 페이지로, 에러 메시지 포함
            return render_template('login.html', error="아이디를 찾지 못했습니다.")

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)