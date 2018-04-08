"""

Установить django или проверить текущую версию.
Подключить python и скачать 'import django', проверить версию 'django.get_version()'

django-admin.exe startproject <name> | создать проект
python manage.py runserver | запустить сервер
LANGUAGE_CODE = 'ru-ru' | поменять язык на русский в settings.py
python manage.py startapp <name> | запустить первое приложение
python manage.py migrate | отправить уже созданные миграции на сервер
python manage.py createsuperuser | создать суперюзера для админки

from django.http import HttpResponse
def index(request):
  return HttpRespon/se('HI!') | создать первое представление / приведен пример
подключить новое приложение в settings.py: INSTALLED_APPS
в главном urls.py прописать include для нового файла urls.py, который нужно создать в папке приложения.
в этом файле нужно пропивать:






















"""