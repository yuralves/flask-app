from flask_sqlalchemy import SQLAlchemy
import settings
from celery import Celery
from flask_caching import Cache


celery = Celery('app', broker=settings.REDIS_URL, result_backend=settings.REDIS_URL)
db = SQLAlchemy()
cache = Cache(
    config=settings.CACHE_CONFIG
)
