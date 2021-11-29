from flask import Flask
from flask_cors import CORS
from app.apis import blueprint
from app.src import db, cache, celery
import settings
from app.converters.date_converter import DateConverter


# INIT APP
def create_app():
    app = Flask(__name__)

    # CORS CONFIG
    CORS(app)

    # DB CONFIG
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # CACHING CONFIG
    cache.init_app(app)

    # CELERY CONFIG
    app.config['redis_max_connections'] = 5
    app.config['broker_pool_limit'] = 5
    celery.conf.update(app.config)

    # GENERAL CONFIG
    app.url_map.converters['date'] = DateConverter
    app.register_blueprint(blueprint, url_prefix='/api')
    return app
