# Django Quotes and Blogs

This application is for storing good quotes and blogs and building a database around it.

## Getting Started

### Configure database in django_quotes_blogs/settings.py

In settings.py, one needs to configure the database configuration and engine accordingly.

### Database migration

```
python manage.py makemigrations quotes

python manage.py sqlmigrate quotes 0001

python manage.py migrate

```

#### Creating superuser
```
python manage.py createsuperuser
```


### Running server

```
python manage.py runserver
```