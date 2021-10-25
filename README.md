#Gesasso

## Requirements

- `docker`

## Get started

Gesasso's project is containerized with Docker, so you can start and init the django app with the following commands:

```bash
$ docker compose up -d
$ docker compose run --rm web python manage.py migrate
$ docker compose run --rm web python manage.py createsuperuser --username gesasso --email gesasso@assos.utc.fr --skip-checks
```

## Urls

One the project is initialized, you can go to theses urls to work:

- `http://localhost:8003` for the api
- `http://localhost:8080` for adminer

## Code style check commands

- Code format `docker compose run --rm web black /code`
- Code style `docker compose run --rm web flake8 gesasso`
- Generate openApi file `docker compose run --rm web ./manage.py generateschema --file openapi-schema.yml`
