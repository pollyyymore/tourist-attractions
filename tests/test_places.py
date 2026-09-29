"""Тесты класса Place и функций работы с местами."""
from models import Place
from models.places import (
    add_place,
    filter_by_category,
    filter_by_rating,
    filter_by_region,
    find_place,
    get_average_rating,
    get_categories_stat,
    sort_places,
)


def test_place_creation():
    place = Place(1, "Гора Эльбрус", "КБР", "гора", "Вершина.", 4.9)
    assert place.id == 1
    assert place.name == "Гора Эльбрус"
    assert place.region == "КБР"
    assert place.category == "гора"
    assert place.rating == 4.9


def test_place_matches_query():
    place = Place(1, "Гора Эльбрус", "КБР", "гора", "Вершина.", 4.9)
    assert place.matches_query("эльбрус")
    assert not place.matches_query("байкал")


def test_place_has_rating_at_least():
    place = Place(1, "Гора Эльбрус", "КБР", "гора", "Вершина.", 4.9)
    assert place.has_rating_at_least(4.0)
    assert not place.has_rating_at_least(5.0)


def test_place_validate_rating():
    assert Place.validate_rating(4.5)
    assert not Place.validate_rating(5.5)


def test_add_place():
    places = []
    place = add_place(places, "Гора Эльбрус", "КБР", "гора", "Вершина.", 4.9)
    assert len(places) == 1
    assert place is places[0]


def test_find_and_filter():
    places = []
    add_place(places, "Эрмитаж", "Санкт-Петербург", "музей", "Музей.", 4.8)
    add_place(places, "Русский музей", "Санкт-Петербург", "музей", "Музей.", 4.7)
    add_place(places, "Гора Эльбрус", "КБР", "гора", "Вершина.", 4.9)

    assert len(find_place(places, "музей")) == 1
    assert len(filter_by_region(places, "Санкт-Петербург")) == 2
    assert len(filter_by_category(places, "гора")) == 1
    assert len(filter_by_rating(places, 4.8)) == 2


def test_sort_and_statistics():
    places = []
    add_place(places, "A", "Регион", "парк", "Описание.", 3.5)
    add_place(places, "B", "Регион", "парк", "Описание.", 4.9)
    add_place(places, "C", "Регион", "музей", "Описание.", 4.2)

    sorted_places = sort_places(places)
    assert sorted_places[0].name == "B"
    assert sorted_places[-1].name == "A"

    stats = get_categories_stat(places)
    assert stats["парк"] == 2
    assert stats["музей"] == 1
    assert get_average_rating(places) == 4.2