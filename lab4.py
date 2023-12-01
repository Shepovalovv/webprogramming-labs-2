from flask import Blueprint, redirect, url_for, render_template, request
lab4 = Blueprint('lab4', __name__)


@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET', 'POST'])
def login():
    error = {}
    if request.method == 'GET':
        return render_template("login.html", error = error)
    
    
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'alex' and password == '123':
        return render_template('success2.html')
    

    error['userpass'] = 'Неверные логин и/или пароль'
    if  username == '':
        error['emptyuser'] = 'не введён логин'

    if password == '':
        error['emptypass'] = 'Не введён пароль'
    return render_template('login.html', error=error, username=username, password=password)

    
@lab4.route('/lab4/fridge', methods=['GET', 'POST'])
def fridge():
    errors = {}
    if request.method == 'GET':
        return render_template("fridge.html", errors=errors)
    temp = request.form.get('temp')
    if temp:
        temp = int(temp)
    return render_template("fridge.html", temp=temp, errors=errors)


