from flask import Blueprint
from flask_restx import Api
from app.auth import authorizations
import settings

from .health import api as hc

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    blueprint,
    title='FLASK-APP',
    version='1.0.0',
    description='Webserver with a task manager',
    authorizations=authorizations,
    doc=settings.SHOW_SWAGGER
)

api.add_namespace(hc, path='/health')
