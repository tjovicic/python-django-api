# Example of an API written in Python and Django


## Start

If you added a new package, force build:

`docker-compose up --build`

else:

`docker-compose up`

## Stop

`docker-compose down`

## First steps

- Adjust your models

- Create migrations: `docker-compose exec web python manage.py makemigrations`

- Migrate: `docker-compose exec web python manage.py migrate`

- Create superuser: `docker-compose exec web python manage.py createsuperuser`

## Inspect API

`http://localhost:8000/api/v1`

## Multiple apps

If you plan to have multiple apps in this project, maybe create
a dedicated "api" app that hosts all other API url routes
