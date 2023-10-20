from flask import Flask, redirect, url_for, render_template
from lab1 import lab1

app = Flask(__name__)
app.register_blueprint(lab1)


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

@app.route('/lab2/')
def lab():
    return render_template('lab2.html')

@app.route('/lab2/lol')
def lol():
    return render_template('lol.html')

