from flask_restx import Namespace, Resource
from app.src.tasks.test_tasks.test import test_task

api = Namespace(
    'Health',
    description='Check workers availability'
)


@api.route('/')
class Health(Resource):
    def get(self):
        '''Waitress health check'''
        return {'success': True}, 200


@api.route('/tasks')
class Tasks(Resource):
    def get(self):
        '''Celery task manager health check'''
        test_task.apply_async()
        return {'success': True}, 200
