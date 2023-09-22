import pytest
from .connection import DBConnectionhandler


@pytest.mark.skip(reason='sensive test')
def test_create_database_engine():
    db_connection_handler = DBConnectionhandler()
    engine = db_connection_handler.get_engine()

    assert engine is not None
