from places import (
    add_place,
    find_place,
    filter_by_region,
    filter_by_category,
    filter_by_rating,
    sort_places,
    get_average_rating,
    get_categories_stat,
)


def test_add_place():
    places = {}
    place_id = add_place(
        places, "Гора Эльбрус", "Кабардино-Балкария",
        "гора", "Высочайшая вершина Европы.", 4.9,
    )
    assert place_id == 1
    assert len(places) == 1
    assert places[1]["name"] == "Гора Эльбрус"


def test_find_place():
    places = {}
    add_place(places, "Озеро Байкал", "Иркутская область",
              "озеро", "Самое глубокое озеро.", 5.0)
    assert find_place(places, "байкал")
    assert not find_place(places, "эльбрус")


def test_filter_by_region_and_category():
    places = {}
    add_place(places, "Эрмитаж", "Санкт-Петербург", "музей", "Музей.", 4.8)
    add_place(places, "Русский музей", "Санкт-Петербург", "музей", "Музей.", 4.7)
    add_place(places, "Гора Эльбрус", "Кабардино-Балкария", "гора", "Вершина.", 4.9)

    assert len(filter_by_region(places, "Санкт-Петербург")) == 2
    assert len(filter_by_category(places, "музей")) == 2
    assert len(filter_by_category(places, "гора")) == 1


def test_filter_and_sort_by_rating():
    places = {}
    add_place(places, "Место A", "Регион", "парк", "Описание.", 3.5)
    add_place(places, "Место B", "Регион", "парк", "Описание.", 4.9)
    add_place(places, "Место C", "Регион", "парк", "Описание.", 4.2)

    assert len(filter_by_rating(places, 4.0)) == 2
    sorted_places = sort_places(places)
    assert sorted_places[0]["name"] == "Место B"
    assert sorted_places[-1]["name"] == "Место A"


def test_statistics():
    places = {}
    add_place(places, "A", "Регион", "парк", "Описание.", 5.0)
    add_place(places, "B", "Регион", "парк", "Описание.", 3.0)
    add_place(places, "C", "Регион", "музей", "Описание.", 4.0)

    assert get_average_rating(places) == 4.0
    stats = get_categories_stat(places)
    assert stats["парк"] == 2
    assert stats["музей"] == 1
