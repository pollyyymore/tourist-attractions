"""Тесты класса Favorite и функций работы с избранным."""
from datetime import date

from models import Place, User
from models.favorites import (
    add_to_favorites,
    cancel_favorite,
    is_place_available,
)


def _make_place() -> Place:
    return Place(1, "Гора Эльбрус", "КБР", "гора", "Вершина.", 4.9)


def _make_user() -> User:
    return User(1, "Иван", "ivan@example.com")


def test_is_place_available_empty():
    favorites = []
    assert is_place_available(favorites, _make_place(), date(2026, 7, 20))


def test_duplicate_favorite_forbidden():
    favorites = []
    place = _make_place()
    user = _make_user()
    add_to_favorites(favorites, place, user, date(2026, 7, 20))
    assert not is_place_available(favorites, place, date(2026, 7, 20))


def test_cancel_favorite_frees_place():
    favorites = []
    place = _make_place()
    user = _make_user()
    favorite = add_to_favorites(favorites, place, user, date(2026, 7, 20))
    assert favorite is not None
    assert cancel_favorite(favorites, favorite.id)
    # после отмены место снова доступно на ту же дату
    assert is_place_available(favorites, place, date(2026, 7, 20))
    # объект не удалён из коллекции
    assert favorite in favorites
    assert favorite.is_cancelled