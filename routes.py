from app import app  # импортируем переменную-сайт

from flask import render_template, redirect, url_for


@app.route('/')  # что будет, если зайти на главную страницу сайта  vk.com/ <-
def index():
    context = {'title': 'My first site'}  # набор элементов, передаваемый в шаблон сайта
    return render_template('index.html', context=context)  # при переходе на главную страницу, показать шаблон index.html


@app.route('/contacts')
def contacts():
    context = {'title': 'Contacts page'}  # набор элементов, передаваемый в шаблон сайта
    return render_template('contacts.html', context=context)


