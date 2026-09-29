"""Сохранение и загрузка данных каталога в JSON-файлах.

Здесь выполняется преобразование:
  JSON → объекты Place / User / Favorite
  объекты → JSON
"""
import json
import os
from typing import List

from models import Favorite, Place, User
from models.places import find_place_by_id
from models.users import find_user_by_id


# --- Places --------------------------------------------------------------


def load_places(filename: str) -> List[Place]:
    """Загрузить места из JSON и преобразовать в объекты Place."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Place.from_data(item) for item in data]
    except (json.JSONDecodeError, ValueError, KeyError, OSError) as error:
        print(f"Не удалось загрузить места: {error}")
        return []


def save_places(filename: str, places: List[Place]) -> None:
    """Сохранить список объектов Place в JSON."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data = [
        {
            "id": place.id,
            "name": place.name,
            "region": place.region,
            "category": place.category,
            "description": place.description,
            "rating": place.rating,
        }
        for place in places
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


# --- Users ---------------------------------------------------------------


def load_users(filename: str) -> List[User]:
    """Загрузить пользователей из JSON и преобразовать в объекты User."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [User.from_data(item) for item in data]
    except (json.JSONDecodeError, ValueError, KeyError, OSError) as error:
        print(f"Не удалось загрузить пользователей: {error}")
        return []


def save_users(filename: str, users: List[User]) -> None:
    """Сохранить список объектов User в JSON."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data = [
        {"id": user.id, "name": user.name, "email": user.email}
        for user in users
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


# --- Favorites -----------------------------------------------------------


def load_favorites(
    filename: str,
    places: List[Place],
    users: List[User],
) -> List[Favorite]:
    """Загрузить избранное из JSON и восстановить связи с Place и User."""
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Не удалось загрузить избранное: {error}")
        return []

    favorites: List[Favorite] = []
    for item in data:
        place = find_place_by_id(places, item["place_id"])
        user = find_user_by_id(users, item["user_id"])
        if place is None or user is None:
            # пропускаем записи, для которых нет связанных объектов
            continue
        favorite = Favorite(
            favorite_id=item["id"],
            place=place,
            user=user,
            visit_date=item["visit_date"],
        )
        favorite.is_cancelled = item.get("is_cancelled", False)
        favorites.append(favorite)
    return favorites


def save_favorites(filename: str, favorites: List[Favorite]) -> None:
    """Сохранить объекты Favorite в JSON (храним только id связанных объектов)."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    data = [
        {
            "id": item.id,
            "place_id": item.place.id,
            "user_id": item.user.id,
            "visit_date": item.visit_date,
            "is_cancelled": item.is_cancelled,
        }
        for item in favorites
    ]
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)