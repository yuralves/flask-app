from sqlalchemy.exc import IntegrityError
from app.src.models.users import Users
from datetime import datetime, timedelta


class UserRepository:

    @staticmethod
    def get():
        """Query all users."""
        users = []
        for user in Users().select_all():
            users.append({
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'updated_at': user.updated_at.strftime('%Y-%m-%d %H:%M:%S')
            })

        return users
