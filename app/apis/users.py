from flask_restx import Namespace, Resource
from app.src.repositories.users import UserRepository as Users


api = Namespace(
    'Users',
    description='Users handling endpoint'
)


@api.route('/')
class User(Resource):
    def get(self):
        '''Get all the users'''
        return Users().get(), 200
