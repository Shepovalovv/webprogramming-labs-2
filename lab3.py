from flask import Blueprint, redirect, url_for, render_template, request
lab3 = Blueprint('lab3', __name__)

@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'

    sex = request.args.get('sex')
    return render_template ('form1.html', user=user, age=age, sex=sex, errors=errors)


@lab3.route('/lab3/order')
def order():
    return render_template('order.html')


@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffee':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10
    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')


@lab3.route('/lab3/buyticket')
def buyticket():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'
    age = request.args.get('age')
    if age == '':
        errors['age'] = 'Заполните поле!'
    exitt = request.args.get('exitt')
    if exitt == '':
        errors['exitt'] = 'Заполните поле!'
    finish = request.args.get('finish')
    if finish == '':
        errors['finish'] = 'Заполните поле!'
    data = request.args.get('data')
    if data == '':
        errors['data'] = 'Заполните поле!'
    baggage = request.args.get('baggage')
    polka = request.args.get('polka')
    tickets = ''
    ticket = request.args.get('ticket')
    if ticket == 'child':
        tickets = 'Детский'
    else:
        tickets = 'Взрослый'
    
    return render_template('buyticket.html', tickets=tickets, polka=polka, baggage=baggage,
                            user=user, age=age, exitt=exitt, finish=finish, data=data, errors=errors)


@lab3.route('/lab3/final')
def final():
    return render_template('final.html')

