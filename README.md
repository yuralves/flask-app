# FLASK-APP

A simple, production ready (i think), Flask App with a lot of nice features to make it even nicer.

## Running the app
This app runs with flask (served by waitress), using a postgresql as the main database, redis as the cache system and celery as the task manager.
This app requires the following env variables to run locally. You can hardcode all of them in [`settings.py`](./settings.py), but i strongly discourage this:

Variable | Description | Type
--- | --- | ---
API_KEY | The key to authenticate api calls | String
POSTGRESQL_USER | PG user | String
POSTGRESQL_PASSWORD | PG password | String
POSTGRESQL_HOST | PG host | String (digits only)
POSTGRESQL_DATABASE | PG database (usually postgresql) | String
REDIS_HOST | Redis host | String
REDIS_PORT | Redis port (6379) | String (digits only)
REDIS_DB | Redis database (usually 0) | String
REDIS_PASSWORD | Redis password | String
ENVIRONMENT | Which environment you are running the app at | LOCAL
MS_HOST | Where to run the service. It defaults to 0.0.0.0 | String
MS_PORT | In which port the service will run. It defaults to 5000 | String

With the variables set, you need to start the Redis and Postgresql prior to starting the server (it won't load otherwise).
Finally, you can start the flask server. Waitress will simulate the WSGI:
```bash
waitress-serve application:app
```
but running it with plain flask will enable hot reload, which is great for debbuging:
```bash
python3 application.py
```

If required, you can then start the celery task manager:
```bash
celery -A celery_worker.celery worker --pool=solo --loglevel=info
```

## Methods
Few things in life are more certain than death. One of them is that i will forget to update this session in the readme. Because of my sheer incompetence, the swagger is autogenerated in the root when running the app locally at `0.0.0.0:5000/api/doc`. Also, there is a swagger and a postman v1 collection in the [`dist`](./dist) directory. Postman is rendering very poorly the swagger file and this framework only allows for Postman v1, so i recommend using other software (preferably self hosted because security) to run it.

## Folder Structure
```.
├── app
│   ├── apis                # routes
│   ├── auth                # authentification methods
│   ├── converters          # some additional url datatype validators
│   └── src
│       ├── models          # database tables models
│       ├── repositories    # essentially the controllers
│       ├── services        # external services, like connecting to Receita Federal, Pipefy and such
│       └── tasks           # asynchronous tasks
├── assets                  # images for the README.md
├── schema                  # database structure and db stored queries
├── tests                   # erm... tests?
└── settings.py             # default configs for the application to run
```

## How does this work?
This is a [flask](https://pypi.org/project/Flask/) application served by waitress.
It is connected via [SQLAlchemy](https://pypi.org/project/SQLAlchemy/) to a PostgreSQL database and the endpoints query (or insert or updated, but **never** delete) data in this database according to the business rules.
To decrease overhead of other services using this, a caching system was required. Hence, this uses [flask_caching](https://pypi.org/project/Flask-Caching/) to cache data in Redis.
Also, some asynchronous needed to be made. Because of that, a [celery](https://pypi.org/project/celery/) worked was implemented to run along with [waitress](https://pypi.org/project/waitress/). This way, long tasks can be ran in the background while shorter requests are still answered "immediately"