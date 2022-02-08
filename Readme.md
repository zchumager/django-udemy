### Installation
Install pyenv
Install latest python version
Install pipenv with pip

Generate Pipfile with pipenv
> python -m pipenv install

Install latest django version 3 with pipenv
> python -m pipenv install Django==3.2.12

---

### Django Setup

Create django project called movies
> django-admin startproject movies.

Create app called api
> cd movies
> django-admin start app api

Create superuser admin
> cd ..
> python manage.py migrate
> python manage.py createsuperuser

Change name into ApiConfig which is in movies.api.apps.py from 'api' to 'movies.api'

Add app into INSTALLED_APPS on settings.py
> movies.api

Register Movie model in admin.py
> from movies.app.models import Movie
> admin.site.register(Movie)

Make migrations
> python manage.py makemigrations
> python manage.py migrate --run-syncdb

## Graphene Setup

Install graphene-django
> python -m pipenv install graphene-django

Add graphene_django module into INSTALLED_APPS on settings.py
> graphene_django

Fix django cors error
https://dzone.com/articles/how-to-fix-django-cors-error