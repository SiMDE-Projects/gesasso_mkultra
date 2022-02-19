# Gesasso

## Requirements

- `docker`
- `yarn`

## Get started

1. Gesasso's project is containerized with Docker, so you can start and init the django app by creating
   a `docker-compose.override.yml` file at repository's root containing these values:

```dockerfile
version: "3.8"
services:
  web:
    environment:
      GESASSO_OAUTH_CLIENT_ID: YOUR-CLIENT-ID
      GESASSO_OAUTH_CLIENT_SECRET: YOUR-CLIENT-SECRET
```

2. Then execute theses commands :

```bash
$ docker compose up -d # Start up the docker containers
$ docker compose run --rm web python manage.py migrate # Initialize database
$ docker compose run --rm web python manage.py createsuperuser --username gesasso --email gesasso@assos.utc.fr --skip-checks # Create a local superuser
```

## Urls

One the project is initialized, you can go to theses urls to work:

- `http://localhost:8003` for the api
- `http://localhost:8080` for adminer

## Code style check commands

Pull requests not complying with code repository's format and style rules would be marked as stall until it's fixed.

You can execute `black` and `flake8` with the 2 following commands to automatically lint/fix your code. If you
add/remove/update an API route, you can regenerate the OpenAPI documentation file with the third command.

- Code format `docker compose run --rm web black /code`
- Code style `docker compose run --rm web flake8 gesasso`
- Generate openApi file `docker compose run --rm web ./manage.py generateschema --file openapi-schema.yml`

## Update requirements.txt file

Add package resolution information to the `requirements.in` file. Then compile it
with `docker-compose run --rm web python3 -m piptools compile`
