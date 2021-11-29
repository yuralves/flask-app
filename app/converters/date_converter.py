from datetime import datetime
from werkzeug.routing import BaseConverter, ValidationError
from werkzeug.exceptions import BadRequest


class DateConverter(BaseConverter):
    """Extracts a ISO8601 date from the path and validates it."""

    regex = r'\d{4}-\d{2}-\d{2}'

    def to_python(self, value):
        try:
            return datetime.strptime(value, '%Y-%m-%d')
        except ValueError:
            raise BadRequest()

    def to_url(self, value):
        return value.strftime('%Y-%m-%d')
