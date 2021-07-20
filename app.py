from flask import Flask, render_template, jsonify, request, redirect, session, url_for
from dao import Database2

app = Flask(__name__)
app.secret_key = "loginpslslsldkdkdkdkfj23324-@sldlzzz"

ID = "hello"
PW = "world"


@app.route('/', methods=['get'])
def get():
    return render_template('blank1.html')  

@app.route('/shop', methods=['get'])
def shop():
    if "userId" in session:
        return render_template("shop.html", username = session.get("userId"), login = True)
    else:
        return render_template("login.html", login = False)  

@app.route('/sign', methods=['get'])
def sign():
    return render_template('join.html')  

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
    if Database2.id_check(id) != None:
        return '중복된 아이디입니다.'
    else:
        Database2.insertdb(data)
        return  '가입완료!!'
    # return  Database2.deletedb()

@app.route('/sign_quit', methods=['POST'])
def withdraw():
    id = request.form.get('id')
    Database2.deletedb(id)
    return '회원탈퇴가 완료되었습니다!'

@app.route('/login', methods=['get'])
def login():
    return render_template('login.html')


@app.route('/login_check', methods=['POST'])
def login_check():
    global ID, PW
    _id_ = request.args.get("loginId")
    _password_ = request.args.get("loginPw")

    if ID == _id_ and PW == _password_:
        # print(_id_, _password_)
        session["userID"] = _id_
        return redirect(url_for("shop"))
    else:
        return redirect(url_for("home"))



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")
