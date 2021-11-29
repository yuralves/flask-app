#!/bin/bash

celery -A celery_worker.celery worker --pool=solo --loglevel=info & waitress-serve --port=5000 --host=0.0.0.0 application:app
