import pytest
from main import UserManager


@pytest.fixture
def user_manager():
    return UserManager()


def test_add_user(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") == True
    assert "john@example.com" == user_manager.get_user("john_doe")

    def test_add_duplicate_user(user_manager):
        user_manager.add_user("john_doe", "john@example")
        with pytest.raises(ValueError):
            user_manager.add_user("john_doe", "another@example.com")
#use pytest -q