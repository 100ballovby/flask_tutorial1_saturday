from app import app  # импортируем переменную-сайт
from forms import LoginForm  # импортируем класс формы

from flask import render_template, redirect, url_for, request


@app.route('/')  # что будет, если зайти на главную страницу сайта  vk.com/ <-
def index():
    context = {'title': 'My first site'}  # набор элементов, передаваемый в шаблон сайта
    return render_template('index.html', context=context)  # при переходе на главную страницу, показать шаблон index.html


@app.route('/contacts', methods=['GET', 'POST'])  # учу функцию воспринимать методы отправки формы
def contacts():
    context = {'title': 'Contacts page'}  # набор элементов, передаваемый в шаблон сайта
    user = None
    if request.method == 'POST':  # если нажали кнопку отправки формы
        form = request.form  # связываю данные формы с функцией
        user = {  # записываю данные из полей формы в словарь
            'name': form.get('name'),
            'surname': form.get('surname'),
            'phone': form.get('p_num')
        }
        return render_template('contacts.html', context=context, user=user)
    else:
        return render_template('contacts.html', context=context)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        form = request.form
        query = form.get('search_query')
        return redirect(f'https://google.com/search?q={query}')
    else:
        return render_template('search.html')


@app.route('/login')  # когда пользователь зашел на страницу логина
def login():
    form = LoginForm()  # создаю экземпляр формы
    return render_template('login.html', title='Войти', form=form)  # передаю форму в шаблон
