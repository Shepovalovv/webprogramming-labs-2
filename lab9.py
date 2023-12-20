from flask import Blueprint, render_template, request, jsonify, abort

lab9 = Blueprint('lab9', __name__)


@lab9.route('/lab9/')
def main():
    return render_template('lab9/index.html')


@lab9.app_errorhandler(404)
def not_found(err):
    return render_template('error404.html')


@lab9.app_errorhandler(500)
def error500(err):
    return render_template('error500.html')


@lab9.route('/lab9/500')
def error():
    result = 1 / 0
    return result

@lab9.route('/lab9/new_year.html', methods=['GET', 'POST'])
def new_year():
    new_year = ""
    username = request.form.get('username')
    username2 = request.form.get('username2')
    sex = request.form.get('sex')

    if username and username2 and sex == 'м':
        new_year = f'Желаю, чтобы {username2} был здоровым и счастливым в новом году и много-много деняк! P. S. {username}'

    if username and username2 and sex == 'ж':
        new_year = f'Желаю, чтобы {username2} была здоровой и счастливой в новом году и много-много деняк! P. S. {username}'
    return render_template('new_year.html', new_year=new_year)

