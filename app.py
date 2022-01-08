from flask import Flask


app = Flask(__name__)  # непосредственно сайт


@app.route('/')  # что будет, если зайти на главную страницу сайта  vk.com/ <-
def index():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
