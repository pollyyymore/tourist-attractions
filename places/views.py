"""View-функции приложения places (страницы мест)."""
from django.http import HttpResponse

from homepage.views import page
from models.places import find_place_by_id
from storage import load_places


def places(request):
    """Страница списка туристических мест."""
    items = ""
    for place in load_places("data/places.json"):
        text = (
            f"{place.name} — {place.region}, {place.category} "
            f"(рейтинг {place.rating})"
        )
        items += (
            f'<li class="list-group-item">'
            f'<a href="/places/{place.id}/">{text}</a>'
            f'</li>'
        )
    content = f"""
    <h1>Туристические места</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("TourCatalog — места", content))


def place_detail(request, place_id):
    """Страница конкретного туристического места."""
    places_list = load_places("data/places.json")
    place = find_place_by_id(places_list, place_id)

    if place is None:
        content = """
        <h1 class="text-danger">Место не найдено</h1>
        <a href="/places/" class="btn btn-outline-secondary">
        ← к списку мест
        </a>
        """
        return HttpResponse(
            page("Место не найдено", content),
            status=404,
        )

    content = f"""
    <div class="card">
    <div class="card-body">
    <h5 class="card-title">{place.name}</h5>
    <p class="card-text"><strong>ID:</strong> {place.id}</p>
    <p class="card-text"><strong>Регион:</strong> {place.region}</p>
    <p class="card-text"><strong>Категория:</strong> {place.category}</p>
    <p class="card-text"><strong>Описание:</strong> {place.description}</p>
    <p class="card-text">
    <strong>Рейтинг:</strong>
    <span class="badge bg-primary">{place.rating}</span>
    </p>
    <a href="/places/" class="btn btn-outline-secondary">
    ← к списку мест
    </a>
    </div>
    </div>
    """
    return HttpResponse(
        page(place.name, content),
        status=200,
    )