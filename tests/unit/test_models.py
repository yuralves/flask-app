from app.src.models.users import Users


def test_users(test_client):
    Users().select_one()
