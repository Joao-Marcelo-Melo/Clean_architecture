# from src.infra.db.settings.connection import DBConnectionhandler
from .users_repository import UsersRepository

def test_insert_user():
    mocked_first_name = 'joao'
    mocked_last_name = 'marcelo'
    mocked_age = 18

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_first_name, mocked_last_name, mocked_age)
