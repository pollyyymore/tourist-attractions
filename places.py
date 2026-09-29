"""Функции для работы с каталогом туристических мест."""


def add_place(
    places: dict[int, dict],
    name: str,
    region: str,
    category: str,
    description: str,
    rating: float,
) -> int:
    """Добавить место в каталог. Вернуть его идентификатор."""
    place_id = max(places.keys(), default=0) + 1
    places[place_id] = {
        "name": name,
        "region": region,
        "category": category,
        "description": description,
        "rating": rating,
    }
    return place_id


def find_place(places: dict[int, dict], query: str) -> list[dict]:
    """Найти места по подстроке в названии (без учёта регистра)."""
    query_lower = query.lower()
    return [
        {"id": place_id, **place}
        for place_id, place in places.items()
        if query_lower in place["name"].lower()
    ]


def filter_by_region(places: dict[int, dict], region: str) -> list[dict]:
    """Отобрать места по региону."""
    region_lower = region.lower()
    return [
        {"id": place_id, **place}
        for place_id, place in places.items()
        if place["region"].lower() == region_lower
    ]


def filter_by_category(places: dict[int, dict], category: str) -> list[dict]:
    """Отобрать места по категории (генератор внутри)."""
    category_lower = category.lower()
    return [
        {"id": place_id, **place}
        for place_id, place in places.items()
        if place["category"].lower() == category_lower
    ]


def filter_by_rating(places: dict[int, dict], min_rating: float) -> list[dict]:
    """Отобрать места с рейтингом не ниже min_rating."""
    return [
        {"id": place_id, **place}
        for place_id, place in places.items()
        if place["rating"] >= min_rating
    ]


def sort_places(places: dict[int, dict]) -> list[dict]:
    """Отсортировать места по рейтингу (по убыванию)."""
    return sorted(
        ({"id": place_id, **place} for place_id, place in places.items()),
        key=lambda place: place["rating"],
        reverse=True,
    )


def get_average_rating(places: dict[int, dict]) -> float:
    """Вернуть средний рейтинг всех мест каталога."""
    if not places:
        return 0.0
    total = sum(place["rating"] for place in places.values())
    return round(total / len(places), 2)


def get_categories_stat(places: dict[int, dict]) -> dict[str, int]:
    """Вернуть статистику: сколько мест в каждой категории."""
    stats: dict[str, int] = {}
    for place in places.values():
        category = place["category"]
        stats[category] = stats.get(category, 0) + 1
    return stats
