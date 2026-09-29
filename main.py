"""Точка запуска приложения «Каталог туристических мест» (ООП-версия)."""
from typing import List

from models import Favorite, Place, User
from models.places import (
    add_place,
    filter_by_category,
    filter_by_rating,
    filter_by_region,
    find_place,
    find_place_by_id,
    get_average_rating,
    get_categories_stat,
    show_places,
    sort_places,
)
from models.users import (
    add_user,
    find_user_by_id,
    show_users,
)
from models.favorites import (
    add_to_favorites,
    cancel_favorite,
    get_favorite_status,
    is_place_available,
    show_favorites,
)
from storage import (
    load_favorites,
    load_places,
    load_users,
    save_favorites,
    save_places,
    save_users,
)
from utils import input_date, input_float, input_int, input_non_empty

PLACES_FILE = "data/places.json"
USERS_FILE = "data/users.json"
FAVORITES_FILE = "data/favorites.json"


def show_short_places(places: List[Place]) -> None:
    """Кратко вывести список объектов Place."""
    if not places:
        print("Ничего не найдено.")
        return
    for place in places:
        print(place)


def create_new_favorite(
    favorites: List[Favorite],
    places: List[Place],
    users: List[User],
) -> None:
    """Организовать пользовательский сценарий добавления места в избранное."""
    place_id = input_int("ID места: ")
    place = find_place_by_id(places, place_id)
    if place is None:
        print("Место не найдено.")
        return

    user_id = input_int("ID пользователя: ")
    user = find_user_by_id(users, user_id)
    if user is None:
        print("Пользователь не найден.")
        return

    visit_date = input_date("Дата посещения (ДД.ММ.ГГГГ): ")

    favorite = add_to_favorites(favorites, place, user, visit_date)
    if favorite is not None:
        print(f"Место добавлено в избранное, запись №{favorite.id}.")
    else:
        print(get_favorite_status(False))


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
    print("8.  Показать пользователей")
    print("9.  Добавить пользователя")
    print("10. Добавить место в избранное")
    print("11. Отменить запись избранного")
    print("12. Показать избранное")
    print("13. Средний рейтинг каталога")
    print("14. Статистика по категориям")
    print("0.  Выход")


def main() -> None:
    """Точка запуска: меню приложения и вызов функций проекта."""
    places: List[Place] = load_places(PLACES_FILE)
    users: List[User] = load_users(USERS_FILE)
    favorites: List[Favorite] = load_favorites(
        FAVORITES_FILE, places, users
    )

    while True:
        show_menu()
        choice = input_int("Выберите действие: ")

        if choice == 0:
            save_places(PLACES_FILE, places)
            save_users(USERS_FILE, users)
            save_favorites(FAVORITES_FILE, favorites)
            print("Данные сохранены. До встречи!")
            break

        elif choice == 1:
            show_places(places)

        elif choice == 2:
            query = input_non_empty("Подстрока названия: ")
            show_short_places(find_place(places, query))

        elif choice == 3:
            region = input_non_empty("Регион: ")
            show_short_places(filter_by_region(places, region))

        elif choice == 4:
            category = input_non_empty("Категория: ")
            show_short_places(filter_by_category(places, category))

        elif choice == 5:
            min_rating = input_float("Минимальный рейтинг: ")
            show_short_places(filter_by_rating(places, min_rating))

        elif choice == 6:
            show_short_places(sort_places(places))

        elif choice == 7:
            name = input_non_empty("Название: ")
            region = input_non_empty("Регион: ")
            category = input_non_empty("Категория: ")
            description = input_non_empty("Описание: ")
            rating = input_float("Рейтинг (0–5): ")
            if not Place.validate_rating(rating):
                print("Рейтинг должен быть в диапазоне 0..5.")
                continue
            place = add_place(
                places, name, region, category, description, rating
            )
            print(f"Место добавлено. ID = {place.id}")

        elif choice == 8:
            show_users(users)

        elif choice == 9:
            name = input_non_empty("Имя: ")
            email = input_non_empty("Email: ")
            user = add_user(users, name, email)
            print(f"Пользователь добавлен. ID = {user.id}")

        elif choice == 10:
            create_new_favorite(favorites, places, users)

        elif choice == 11:
            favorite_id = input_int("ID записи избранного: ")
            if cancel_favorite(favorites, favorite_id):
                print("Запись отменена.")
            else:
                print("Запись не найдена.")

        elif choice == 12:
            show_favorites(favorites)

        elif choice == 13:
            print(f"Средний рейтинг каталога: {get_average_rating(places)}")

        elif choice == 14:
            stats = get_categories_stat(places)
            if not stats:
                print("Нет данных.")
            for category, count in stats.items():
                print(f"{category}: {count}")

        else:
            print("Неизвестная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()