
Доступ в админ-панель: polina / qwerty

#ЗАПУСК ПРОЕКТА MACOS

```
python3 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
cd my_site
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

```
CSS через STATIC добавлены в base.html и publishers.html
Шаблон base.html используется в publishers.html
Добавлена возможность загружать картинки к книгам
```
