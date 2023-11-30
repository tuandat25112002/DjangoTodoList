
// create django-admin project
django-admin startproject django_todo_app
// move into this project
cd django_todo_app
// migrate database
python manage.py migrate
// run server
python manage.py runserver
// create superuser
winpty python manage.py createsuperuser
// create new migration
python manage.py makemigrations
