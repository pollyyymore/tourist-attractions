"""Точка запуска приложения «Каталог туристических мест»."""
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
from favorites import (
    add_to_favorites,
    remove_from_favorites,
    get_favorite_status,
)
from storage import (
    load_places, save_places,
    load_favorites, save_favorites,
)
from utils import input_int, input_float, input_date, input_non_empty

PLACES_FILE = "data/places.json"
FAVORITES_FILE = "data/favorites.json"


def show_places(places: dict[int, dict]) -> None:
    """Вывести список мест каталога в виде таблицы."""
    if not places:
        print("Каталог пуст.")
        return
    print(f"{'ID':<4}{'Название':<28}{'Регион':<22}{'Категория':<14}{'Рейтинг':<8}")
    print("-" * 76)
    for place_id, place in places.items():
        print(
            f"{place_id:<4}{place['name']:<28}"
            f"{place['region']:<22}{place['category']:<14}"
            f"{place['rating']:<8}"
        )


def show_places_short(items: list[dict]) -> None:
    """Кратко вывести найденные/отфильтрованные места."""
    if not items:
        print("Ничего не найдено.")
        return
    for place in items:
        print(
            f"ID {place['id']}: {place['name']} — {place['region']}, "
            f"{place['category']}, рейтинг {place['rating']}"
        )


def show_favorites(favorites: list[dict], places: dict[int, dict]) -> None:
    """Вывести список избранных мест."""
    if not favorites:
        print("Список избранного пуст.")
        return
    print(f"{'ID':<4}{'Место':<30}{'Дата посещения':<16}")
    print("-" * 50)
    for item in favorites:
        place = places.get(item["place_id"], {"name": "—"})
        print(f"{item['id']:<4}{place['name']:<30}{item['date']:<16}")


def show_menu() -> None:
    """Вывести меню приложения."""
    print("\n=== Каталог туристических мест ===")
    print("1.  Показать все места")
    print("2.  Найти место по названию")
    print("3.  Фильтр по региону")
    print("4.  Фильтр по категории")
    print("5.  Фильтр по рейтингу")
    print("6.  Сортировать по рейтингу")
    print("7.  Добавить новое место")
    print("8.  Добавить место в избранное")
    print("9.  Удалить место из избранного")
    print("10. Показать избранное")
    print("11. Средний рейтинг каталога")
    print("12. Статистика по категориям")
    print("0.  Выход")


def main() -> None:
    """Точка запуска: меню приложения и вызов функций проекта."""
    places = load_places(PLACES_FILE)
    favorites = load_favorites(FAVORITES_FILE)

    while True:
        show_menu()
        choice = input_int("Выберите действие: ")

        if choice == 0:
            save_places(PLACES_FILE, places)
            save_favorites(FAVORITES_FILE, favorites)
            print("Данные сохранены. До встречи!")
            break

        elif choice == 1:
            show_places(places)

        elif choice == 2:
            query = input_non_empty("Подстрока названия: ")
            show_places_short(find_place(places, query))

        elif choice == 3:
            region = input_non_empty("Регион: ")
            show_places_short(filter_by_region(places, region))

        elif choice == 4:
            category = input_non_empty("Категория (гора, озеро, музей, парк): ")
            show_places_short(filter_by_category(places, category))

        elif choice == 5:
            min_rating = input_float("Минимальный рейтинг: ")
            show_places_short(filter_by_rating(places, min_rating))

        elif choice == 6:
            show_places_short(sort_places(places))

        elif choice == 7:
            name = input_non_empty("Название: ")
            region = input_non_empty("Регион: ")
            category = input_non_empty("Категория: ")
            description = input_non_empty("Описание: ")
            rating = input_float("Рейтинг (0–5): ")
            place_id = add_place(
                places, name, region, category, description, rating
            )
            print(f"Место добавлено. ID = {place_id}")

        elif choice == 8:
            place_id = input_int("ID места: ")
            visit_date = input_date("Дата посещения (ДД.ММ.ГГГГ): ")
            item = add_to_favorites(favorites, place_id, visit_date)
            if item:
                print(f"Место добавлено в избранное, запись №{item['id']}.")
            else:
                print(get_favorite_status(False))

        elif choice == 9:
            favorite_id = input_int("ID записи избранного: ")
            if remove_from_favorites(favorites, favorite_id):
                print("Запись удалена из избранного.")
            else:
                print("Запись не найдена.")

        elif choice == 10:
            show_favorites(favorites, places)

        elif choice == 11:
            print(f"Средний рейтинг каталога: {get_average_rating(places)}")

        elif choice == 12:
            stats = get_categories_stat(places)
            if not stats:
                print("Нет данных.")
            for category, count in stats.items():
                print(f"{category}: {count}")

        else:
            print("Неизвестная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()
