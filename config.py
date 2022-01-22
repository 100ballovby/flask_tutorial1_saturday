# файл конфигурации сайта (все настройки здесь)
import os


class Config:
    # все параметры конфигурации определяются как переменные класса
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'try-to-guess'

