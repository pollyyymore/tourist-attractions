"""Класс Place и функции работы с туристическими местами."""
from typing import List


class Place:
    """Туристическое место в каталоге."""

    def __init__(
        self,
        place_id: int,
        name: str,
        region: str,
        category: str,
        description: str,
        rating: float,
    ) -> None:
        """Создать объект туристического места."""
        self.id = place_id
        self.name = name
        self.region = region
        self.category = category
        self.description = description
        self.rating = rating

    def matches_query(self, query: str) -> bool:
        """Проверить, встречается ли подстрока в названии места."""
        return query.lower() in self.name.lower()

    def has_rating_at_least(self, min_rating: float) -> bool:
        """Проверить, что рейтинг места не ниже указанного значения."""
        return self.rating >= min_rating

    def __str__(self) -> str:
        """Вернуть строковое представление места."""
        return (
            f"{self.name} ({self.region}, {self.category}), "
            f"рейтинг {self.rating}"
        )

    @classmethod
    def from_data(cls, data: dict) -> "Place":
        """Создать объект Place из словаря (например, из json)."""
        return cls(
            place_id=data["id"],
            name=data["name"],
            region=data["region"],
            category=data["category"],
            description=data["description"],
            rating=data["rating"],
        )

    @staticmethod
    def validate_rating(rating: float) -> bool:
        """Проверить, что рейтинг в допустимом диапазоне 0..5."""
        return 0.0 <= rating <= 5.0


# --- Функции работы с коллекцией объектов Place --------------------------


def add_place(
    places: List[Place],
    name: str,
    region: str,
    category: str,
    description: str,
    rating: float,
) -> Place:
    """Создать объект Place и добавить его в коллекцию."""
    place_id = max((place.id for place in places), default=0) + 1
    place = Place(place_id, name, region, category, description, rating)
    places.append(place)
    return place


def find_place(places: List[Place], query: str) -> List[Place]:
    """Найти места по подстроке названия."""
    return [place for place in places if place.matches_query(query)]


def find_place_by_id(places: List[Place], place_id: int) -> Place | None:
    """Найти место по идентификатору."""
    for place in places:
        if place.id == place_id:
            return place
    return None


def filter_by_region(places: List[Place], region: str) -> List[Place]:
    """Отобрать места по региону."""
    region_lower = region.lower()
    return [place for place in places if place.region.lower() == region_lower]


def filter_by_category(places: List[Place], category: str) -> List[Place]:
    """Отобрать места по категории."""
    category_lower = category.lower()
    return [p for p in places if p.category.lower() == category_lower]


def filter_by_rating(places: List[Place], min_rating: float) -> List[Place]:
    """Отобрать места с рейтингом не ниже min_rating (с использованием метода)."""
    return [place for place in places if place.has_rating_at_least(min_rating)]


def sort_places(places: List[Place]) -> List[Place]:
    """Отсортировать места по рейтингу (по убыванию)."""
    return sorted(places, key=lambda place: place.rating, reverse=True)


def get_average_rating(places: List[Place]) -> float:
    """Вернуть средний рейтинг всех мест каталога."""
    if not places:
        return 0.0
    return round(sum(place.rating for place in places) / len(places), 2)


def get_categories_stat(places: List[Place]) -> dict[str, int]:
    """Вернуть статистику: сколько мест в каждой категории."""
    stats: dict[str, int] = {}
    for place in places:
        stats[place.category] = stats.get(place.category, 0) + 1
    return stats


def show_places(places: List[Place]) -> None:
    """Вывести список мест в виде таблицы."""
    if not places:
        print("Каталог пуст.")
        return
    print(
        f"{'ID':<4}{'Название':<28}{'Регион':<22}"
        f"{'Категория':<14}{'Рейтинг':<8}"
    )
    print("-" * 76)
    for place in places:
        print(
            f"{place.id:<4}{place.name:<28}{place.region:<22}"
            f"{place.category:<14}{place.rating:<8}"
        )