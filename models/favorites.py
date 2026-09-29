"""Класс Favorite и функции работы с избранными местами."""
from datetime import date
from typing import List, Optional

from .places import Place
from .users import User


class Favorite:
    """Запись о добавлении места в избранное для посещения."""

    def __init__(
        self,
        favorite_id: int,
        place: Place,
        user: User,
        visit_date: str,
    ) -> None:
        self.id = favorite_id
        self.place = place
        self.user = user
        self.visit_date = visit_date
        self.is_cancelled = False

    def cancel(self) -> None:
        """Отменить запись избранного (не удаляя объект из коллекции)."""
        self.is_cancelled = True

    def __str__(self) -> str:
        """Вернуть строковое представление записи с учётом состояния."""
        state = "отменено" if self.is_cancelled else "активно"
        return (
            f"[{self.id}] {self.place.name} — {self.user.name}, "
            f"{self.visit_date} ({state})"
        )


# --- Функции работы с коллекцией объектов Favorite -----------------------


def is_place_available(
    favorites: List[Favorite],
    place: Place,
    visit_date: date,
) -> bool:
    """Проверить, что место не добавлено в избранное другим пользователем
    на указанную дату (активной записью)."""
    date_str = visit_date.isoformat()
    for item in favorites:
        if (
            item.place.id == place.id
            and item.visit_date == date_str
            and not item.is_cancelled
        ):
            return False
    return True


def add_to_favorites(
    favorites: List[Favorite],
    place: Place,
    user: User,
    visit_date: date,
) -> Optional[Favorite]:
    """Создать объект Favorite, если место свободно на указанную дату."""
    if not is_place_available(favorites, place, visit_date):
        return None
    favorite_id = max((item.id for item in favorites), default=0) + 1
    favorite = Favorite(
        favorite_id=favorite_id,
        place=place,
        user=user,
        visit_date=visit_date.isoformat(),
    )
    favorites.append(favorite)
    return favorite


def cancel_favorite(favorites: List[Favorite], favorite_id: int) -> bool:
    """Найти запись избранного по id и вызвать её метод cancel()."""
    for item in favorites:
        if item.id == favorite_id:
            item.cancel()
            return True
    return False


def get_favorite_status(is_available: bool) -> str:
    """Вернуть текстовый статус места (функция из ПР1, переработанная под тему)."""
    if is_available:
        return "Место доступно для добавления в избранное"
    return "Место уже добавлено в избранное на эту дату"


def show_favorites(favorites: List[Favorite]) -> None:
    """Вывести список избранного."""
    if not favorites:
        print("Список избранного пуст.")
        return
    print(f"{'ID':<4}{'Место':<30}{'Пользователь':<20}{'Дата':<14}{'Статус':<10}")
    print("-" * 78)
    for item in favorites:
        state = "отменено" if item.is_cancelled else "активно"
        print(
            f"{item.id:<4}{item.place.name:<30}{item.user.name:<20}"
            f"{item.visit_date:<14}{state:<10}"
        )