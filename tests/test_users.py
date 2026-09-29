"""Тесты класса User и функций работы с пользователями."""
from models import User
from models.users import add_user, find_user


def test_user_creation():
    user = User(1, "Иван Петров", "ivan@example.com")
    assert user.id == 1
    assert user.name == "Иван Петров"
    assert user.email == "ivan@example.com"


def test_user_from_data():
    data = {"id": 2, "name": "Мария", "email": "maria@example.com"}
    user = User.from_data(data)
    assert user.id == 2
    assert user.name == "Мария"
    assert user.email == "maria@example.com"


def test_add_and_find_user():
    users = []
    user = add_user(users, "Иван", "ivan@example.com")
    assert user in users
    assert len(find_user(users, "иван")) == 1
    assert len(find_user(users, "example.com")) == 1
    assert len(find_user(users, "нет")) == 0