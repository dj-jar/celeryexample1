# celeryexample1

http://redd.it/34rzko

```
git clone https://github.com/dj-jar/celeryexample1.git
cd celeryexample1/
pip install -r pip-requirements.txt
python manage.py makemigrations
python manage.py migrate
celery -A problemproject worker -l info &
python manage.py runserver
```
