"""Функции для работы со списком избранных мест для посещения."""
from datetime import date


def is_in_favorites(
    favorites: list[dict], place_id: int, visit_date: date
) -> bool:
    """Проверить, добавлено ли уже это место в избранное на указанную дату."""
    date_str = visit_date.isoformat()
    for item in favorites:
        if item["place_id"] == place_id and item["date"] == date_str:
            return False
    return True


def add_to_favorites(
    favorites: list[dict], place_id: int, visit_date: date
) -> dict | None:
    """Добавить место в избранное, если оно ещё не добавлено на эту дату."""
    if not is_in_favorites(favorites, place_id, visit_date):
        return None
    favorite_id = max((item["id"] for item in favorites), default=0) + 1
    item = {
        "id": favorite_id,
        "place_id": place_id,
        "date": visit_date.isoformat(),
    }
    favorites.append(item)
    return item


def remove_from_favorites(favorites: list[dict], favorite_id: int) -> bool:
    """Удалить место из избранного по идентификатору записи."""
    for index, item in enumerate(favorites):
        if item["id"] == favorite_id:
            favorites.pop(index)
            return True
    return False


def get_favorite_status(is_available: bool) -> str:
    if is_available:
        return "Место доступно для добавления в избранное"
    return "Место уже добавлено в избранное на эту дату"
