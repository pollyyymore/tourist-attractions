"""View-функции приложения favorites (страницы избранного)."""
from django.http import HttpResponse

from homepage.views import page
from models.favorites import find_favorite_by_id
from storage import load_favorites, load_places, load_users


def favorites(request):
    """Страница списка избранного."""
    places_list = load_places("data/places.json")
    users_list = load_users("data/users.json")
    favorites_list = load_favorites(
        "data/favorites.json", places_list, users_list
    )

    items = ""
    for item in favorites_list:
        status = "отменено" if item.is_cancelled else "активно"
        badge = "bg-secondary" if item.is_cancelled else "bg-success"
        text = f"{item.place.name} — {item.user.name}, {item.visit_date}"
        items += (
            f'<li class="list-group-item">'
            f'<a href="/favorites/{item.id}/">{text}</a> '
            f'<span class="badge {badge}">{status}</span>'
            f'</li>'
        )
    content = f"""
    <h1>Избранное</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("TourCatalog — избранное", content))


def favorite_detail(request, favorite_id):
    """Страница конкретной записи избранного."""
    places_list = load_places("data/places.json")
    users_list = load_users("data/users.json")
    favorites_list = load_favorites(
        "data/favorites.json", places_list, users_list
    )
    favorite = find_favorite_by_id(favorites_list, favorite_id)

    if favorite is None:
        content = """
        <h1 class="text-danger">Запись избранного не найдена</h1>
        <a href="/favorites/" class="btn btn-outline-secondary">
        ← к списку избранного
        </a>
        """
        return HttpResponse(
            page("Запись не найдена", content),
            status=404,
        )

    status = "Удалено" if favorite.is_cancelled else "В избранном"
    badge = "bg-secondary" if favorite.is_cancelled else "bg-success"
    content = f"""
    <div class="card">
    <div class="card-body">
    <h5 class="card-title">Запись №{favorite.id}</h5>
    <p class="card-text">
    <strong>Место:</strong> {favorite.place.name}
    </p>
    <p class="card-text">
    <strong>Пользователь:</strong> {favorite.user.name}
    </p>
    <p class="card-text">
    <strong>Дата посещения:</strong> {favorite.visit_date}
    </p>
    <p class="card-text">
    <strong>Статус:</strong>
    <span class="badge {badge}">{status}</span>
    </p>
    <a href="/favorites/" class="btn btn-outline-secondary">
    ← к списку избранного
    </a>
    </div>
    </div>
    """
    return HttpResponse(
        page(f"Запись №{favorite.id}", content),
        status=200,
    )