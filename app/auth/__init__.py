from functools import wraps
from flask import request, abort
import os

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'x-api-key'
    }
}


def require_appkey(view_function):
    @wraps(view_function)
    def decorated_function(*args, **kwargs):
        if request.headers.get('x-api-key') == os.getenv('API_KEY'):
            return view_function(*args, **kwargs)
        abort(401)
    return decorated_function
