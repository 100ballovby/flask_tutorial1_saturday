from flask import Flask
from flask import render_template


app = Flask(__name__)  # непосредственно сайт

from routes import *

if __name__ == '__main__':
    app.run()
