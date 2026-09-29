from datetime import date
from favorites import (
    is_in_favorites,
    add_to_favorites,
    remove_from_favorites,
)


def test_is_in_favorites_empty():
    favorites = []
    assert is_in_favorites(favorites, 1, date(2026, 7, 20))


def test_duplicate_favorite_forbidden():
    favorites = []
    add_to_favorites(favorites, 1, date(2026, 7, 20))
    assert not is_in_favorites(favorites, 1, date(2026, 7, 20))


def test_remove_from_favorites():
    favorites = []
    item = add_to_favorites(favorites, 1, date(2026, 7, 20))
    assert remove_from_favorites(favorites, item["id"])
    assert is_in_favorites(favorites, 1, date(2026, 7, 20))
