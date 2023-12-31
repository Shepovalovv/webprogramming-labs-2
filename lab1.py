from flask import Blueprint, redirect, url_for
lab1 = Blueprint('lab1', __name__)


@lab1.route("/")
@lab1.route("/index")
def start():
    return redirect("/menu", code=302)


@lab1.route("/menu")
def menu():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
<html>
    <head>
        <title>НГТУ, ФБ, Лабораторные работы</title>
    </head>
    <body>
        <header>
        НГТУ,ФБ, WEB-программирование, часть 2. Список лабораторных
        </header>

        <ul>
            <li>
                <a href = '/lab1' target = _blank>Первая Лабораторная работа</a>
            </li>

            <li>
                <a href = '/lab2' target = _blank>Вторая Лабораторная работа</a>
            </li>

            <li>
                <a href = '/lab3' target = _blank>Третья Лабораторная работа</a>
            </li>

            <li>
                <a href = '/lab4' target = _blank>Четвёртая Лабораторная работа</a>
            </li>

            <li>
                <a href = '/lab5' target = _blank>Пятая Лабораторная работа</a>
            </li>

            <li>
                <a href = '/lab6' target = _blank>Шестая Лабораторная работа</a>
            </li>

             <li>
                <a href = '/lab7' target = _blank>Седьмая Лабораторная работа</a>
            </li>

            <li>
                <a href = '/lab8' target = _blank>Восьмая Лабораторная работа</a>
            </li>

             <li>
                <a href = '/lab9' target = _blank>Девятая Лабораторная работа</a>
            </li>
        </ul>

        <footer>
        &copy; Шеповалов Артём, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1")
def lab():
    return '''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
<html>
    <head>
        <title>Шеповалов Артём Сергеевич, Лабораторная 1</title>
    </head>
    <body>
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервис на flask</h1>
        <h2>Реализованные роуты</h2>

        <a href = "/lab1/oak" target =_blank>Дуб</a><br>
        <a href = "/lab1/student" target =_blank>Студент</a><br>
        <a href = "/lab1/python" target =_blank>Python</a><br>
        <a href = "/lab1/LoL" target =_blank>LoL</a><br>

        <div>
        Flask — фреймворк для создания веб-приложений на языке
        программирования Python, использующий набор инструментов
        Werkzeug, а также шаблонизатор Jinja2. Относится к категории так
        называемых микрофреймворков — минималистичных каркасов
        веб-приложений, сознательно предоставляющих лишь самые базовые возможности.
        </div>

        <a href ="/menu" target =_blank>Меню</a>

        <footer>
        &copy; Шеповалов Артём, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''


@lab1.route("/lab1/oak")
def oak():
    return'''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <h1>Дуб</h1>
        <img src ="''' + url_for('static', filename = 'oak.jpg') +'''">
    </body>
<html>
'''


@lab1.route("/lab1/student")
def student():
    return'''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <h1>Шеповалов Артём Сергеевич</h1>
        <img src ="''' + url_for('static', filename = 'logo.jpg') +'''">
    </body>
<html>
'''


@lab1.route("/lab1/python")
def python():
    return'''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <div>
            Автор языка Python назвал его в честь британского комедийного шоу «Monty Python»,
            которое было популярно в начале 1970-х годов.<br>
            Это телешоу позволяло автору расслабиться и отвлечься от разработки языка.<br>
            Однако, несмотря на настоящее происхождение названия, для людей более очевидно
            связывать Python со словом «змея».<br> Этому также способствует логотип, на котором изображена рептилия.
        </div>
        <img src ="''' + url_for('static', filename = 'python.png') +'''">
    </body>
<html>
'''


@lab1.route("/lab1/LoL")
def LoL():
    return'''
<!doctype html>
<link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
<html>
    <body>
        <div>
            Когда играешь в эту игру, теряешь свои нервы, изматываешь душу.<br>
            Однако, она затягивает, как сделка с дьяволом...<br>
        </div>
        <img src ="''' + url_for('static', filename = 'LoL.jpg') +'''">
    </body>
<html>
'''
