from flask import Flask
from config import Config  # импортирую класс конфигурации в свой сайт


app = Flask(__name__)  # непосредственно сайт
app.config.from_object(Config)  # строю конфигурацию сайта на основе класса конфигурации

from routes import *

if __name__ == '__main__':
    app.run()
