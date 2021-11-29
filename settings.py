import os
import json

"""
DATABASE CONFIGURATION
Creates the connection string to connect to the database.
"""
SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{pwd}@{host}:5432/{db}'.format(
    user=os.getenv('POSTGRESQL_USER'),
    pwd=os.getenv('POSTGRESQL_PASSWORD'),
    host=os.getenv('POSTGRESQL_HOST'),
    db=os.getenv('POSTGRESQL_DATABASE'),
)

"""
REDIS CONFIGURATION
"""
REDIS_HOST = os.getenv('REDIS_HOST')
REDIS_PORT = os.getenv('REDIS_PORT')
REDIS_DB = os.getenv('REDIS_DB')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD')
REDIS_URL = "redis://:{password}@{hostname}:{port}/{db_number}".format(
    password=REDIS_PASSWORD,
    hostname=REDIS_HOST,
    port=REDIS_PORT,
    db_number=REDIS_DB
)

"""
CACHE CONFIGURATION
"""
if os.getenv('ENVIRONMENT') == 'LOCAL':
    CACHE_CONFIG = {
        'CACHE_TYPE': 'SimpleCache',
        'CACHE_DEFAULT_TIMEOUT': 300,
    }
elif os.getenv('ENVIRONMENT') == 'DEVELOPMENT':
    CACHE_CONFIG = {
        'CACHE_TYPE': 'RedisCache',
        'CACHE_REDIS_HOST': REDIS_HOST,
        'CACHE_REDIS_PORT': REDIS_PORT,
        'CACHE_REDIS_PASSWORD': REDIS_PASSWORD,
        'CACHE_REDIS_DB': REDIS_DB,
        'CACHE_REDIS_URL': REDIS_URL,
        'CACHE_DEFAULT_TIMEOUT': 300,
        'CACHE_KEY_PREFIX': 'flask_api_',
    }
else:
    CACHE_CONFIG = {
        'CACHE_TYPE': 'RedisCache',
        'CACHE_REDIS_HOST': REDIS_HOST,
        'CACHE_REDIS_PORT': REDIS_PORT,
        'CACHE_REDIS_PASSWORD': REDIS_PASSWORD,
        'CACHE_REDIS_DB': REDIS_DB,
        'CACHE_REDIS_URL': REDIS_URL,
        'CACHE_DEFAULT_TIMEOUT': 300,
        'CACHE_KEY_PREFIX': 'flask_api_',
    }
CACHING_TIME = 600
