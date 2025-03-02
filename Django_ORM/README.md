# Django


```bash
mkdir www
cd www
python -m venv .venv

pip install django
pip install psycopg-binary
python -m django --version

django-admin startproject writer text.or.kr
cd text.or.kr

python manage.py runserver

python manage.py startapp polls

python manage.py migrate

python manage.py makemigrations polls

python manage.py sqlmigrate polls 0001

python manage.py migrate

python manage.py shell

python manage.py createsuperuser
Username: admin
Email address: admin@vivabj.com
Password: **********
Password (again): *********
Superuser created successfully.
python manage.py runserver
```
