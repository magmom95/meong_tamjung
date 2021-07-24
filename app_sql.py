from flask import Flask, render_template, jsonify, request, session, flash, redirect, url_for
from flask import current_app
from dao import Database2


app = Flask(__name__)
app.secret_key = b'aaa!111/'

# 통계 화면으로 이동
@app.route('/', methods=['get'])
def get():
    return render_template('blank1.html')  

# 쇼핑몰로 이동
@app.route('/shop', methods=['get'])
def shop():
    return render_template('shop.html')  

# 회원가입 화면으로 이동
@app.route('/sign', methods=['get'])
def sign():
    return render_template('join.html')  

# 로그인 화면으로 이동
@app.route('/login', methods=['get'])
def login():
    return render_template('login.html')  

# 회원가입 기능
@app.route('/sign_in', methods=['POST'])
def sign_in():
    # "id=" + id + "&pw=" + pw + "&name=" + name + "&email=" + email
    id = request.form.get('id')
    pw = request.form.get('pw')
    name = request.form.get('name')
    email = request.form.get('email')
    data = (id, pw, name, email)
    print(Database2.email_check(email))
    if Database2.email_check(email) != None:
        return '이미 가입된 이메일 입니다.'
    elif Database2.id_check(id) != None:
        return '중복된 아이디입니다.'
    else:
        Database2.insertdb(data)
        return  '가입완료!!'

# 회원탈퇴
@app.route('/sign_quit', methods=['POST'])
def withdraw():
    id = request.form.get('id')
    Database2.deletedb(id)
    return '회원탈퇴가 완료되었습니다!'

# 로그인 기능
@app.route('/login_check', methods=['POST'])
def login_check():
    id = request.form.get('id')
    pw = request.form.get('pw')
    idpw = (id, pw)
    session.clear()

    # id/pw가 테이블에 존재하면 세션만들기
    if Database2.logindb(idpw) != None:
        print(session)
        session.clear()
        session['user'] = id
        print(session)
        return "로그인이 완료되었습니다!"
    else:
        return "아이디나 비밀번호가 일치하지 않습니다"

# 로그아웃 기능
@app.route('/logout_check', methods=['get'])
def logout():

    session.pop("user")
    return '로그아웃 되었습니다!'

if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")