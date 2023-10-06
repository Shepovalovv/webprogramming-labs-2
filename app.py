from flask import Flask
app = Flask(__name__)

@app.route("/")
def start():
    return """
<!doctype html>
<html>
    <head>
        <tittle>Шеповалов Артём Сергеевич, Лабораторная 1<tittle>
    </head>
    <body>
        <header>
        НГТУ, ФБ, Лабораторная работа 1
        </header>

        <h1>web-сервис на flask</h1>

        <footer>
        &copy; Шеповалов Артём, ФБИ-11, 3 курс, 2023
        </footer>
    </body>
</html>
"""