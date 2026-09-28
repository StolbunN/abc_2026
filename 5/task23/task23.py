# todo: добавьте во Flask маршруты для страниц (endpoint)
# - О компании
# - Контакты
# - Список постов

# Делал в vscode. Перед запуском задания делал следующие команды (Windows):

# 1) создал виртуальное окружение
# python -m venv venv

# 2) активировал окружение
# .\venv\Scripts\activate

# 3) установка flask
# pip install flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Flask!"


@app.route("/about")
def about():
  return "Страница 'О компании'"


@app.route("/contacts")
def contacts():
  return "Страница 'Контакты'"


@app.route("/posts")
def posts():
  return "Страница 'Список постов'"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)