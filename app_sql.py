from flask import Flask, render_template, jsonify, request, Blueprint, flash, redirect, url_for
from flask import current_app
from dao import Database2

app = Flask(__name__)


@app.route('/', methods=['get'])
def get():
    return render_template('blank1.html')  

@app.route('/shop', methods=['get'])
def shop():
    return render_template('shop.html')  

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
# data = ()
    return  Database2.insertdb()
    # return  Database2.deletedb()



if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port="5000")