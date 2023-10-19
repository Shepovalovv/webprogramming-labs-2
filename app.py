from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect("/menu", code=302)

@app.route("/menu")
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
        </ul>

        <footer>
        &copy; Шеповалов Артём, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
'''

@app.route("/lab1")
def lab1():
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

@app.route("/lab1/oak")
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

@app.route("/lab1/student")
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

@app.route("/lab1/python")
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

@app.route("/lab1/LoL")
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

@app.route('/lab2/example')
def example():
    name, labnumber, group, cource = "Шеповалов Артём Сергеевич", 2, "ФБИ-11", "3 курс"
    fruits = [
    {'name': 'яблоки', 'price': 100},
     {'name': 'груши', 'price': 120}, 
     {'name': 'апельсины', 'price': 80}, 
     {'name': 'мандарины', 'price': 95}, 
     {'name': 'манго', 'price': 95}
     ]
    
    books = [
    {'autors': 'Игорь Валериев', 'book': 'Ермак. Личник', 'cat': 'Историческая фантастика', 'str': '333 страниц'},
    {'autors': 'Алекс Миро', 'book': 'Геном: Исцелённые', 'cat': 'Научная фантастика', 'str': '503 страниц'},
    {'autors': 'Василий Головачёв', 'book': 'Очень большой лес', 'cat': 'Боевая фантастика', 'str': '451 страниц'},
    {'autors': 'Жанна Лебедева', 'book': 'Зверь без страха и упрёка', 'cat': 'Любовное фэнтези', 'str': '1158 страниц'},
    {'autors': 'Дэн Симмонс', 'book': 'Сироты Вечности', 'cat': 'Зарубежная фантастика', 'str': '731 страниц'},
    {'autors': 'Патрик Несс', 'book': 'Поступь хаоса', 'cat': 'Зарубежная фантастика', 'str': '496 страниц'},
    {'autors': 'Константин Калбазов', 'book': 'Пандора. Одиссея', 'cat': 'Боевая фантастика', 'str': '879 страниц'},
    {'autors': 'Бернар Вербер', 'book': 'Голос земли', 'cat': 'Зарубежная фантастика', 'str': '843 страниц'},
    {'autors': 'Анатолий Махавкин', 'book': 'Черепа', 'cat': 'Боевое фэнтези', 'str': '534 страниц'},
    {'autors': 'Чэнь Цюфань', 'book': 'Мусорный прибой', 'cat': 'Зарубежная фантастика', 'str': '1076 страниц'}
    ]

    return render_template('example.html',
                            name = name, labnumber = labnumber, group = group, 
                            cource = cource, fruits = fruits, books = books)

