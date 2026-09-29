import json
import os


def load_places(filename: str) -> dict[int, dict]:
    if not os.path.exists(filename):
        return {}
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
            return {int(key): value for key, value in data.items()}
    except (json.JSONDecodeError, ValueError, OSError) as error:
        print(f"Не удалось загрузить места: {error}")
        return {}


def save_places(filename: str, places: dict[int, dict]) -> None:
    """Сохранить места в JSON-файл."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(places, file, ensure_ascii=False, indent=2)


def load_favorites(filename: str) -> list[dict]:
    if not os.path.exists(filename):
        return []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError) as error:
        print(f"Не удалось загрузить избранное: {error}")
        return []


def save_favorites(filename: str, favorites: list[dict]) -> None:
    """Сохранить избранное в JSON-файл."""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(favorites, file, ensure_ascii=False, indent=2)
