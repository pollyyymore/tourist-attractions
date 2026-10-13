"""View-функции приложения users (страницы пользователей)."""
from django.http import HttpResponse

from homepage.views import page
from models.users import find_user_by_id
from storage import load_users


def users(request):
    """Страница списка пользователей каталога."""
    items = ""
    for user in load_users("data/users.json"):
        text = f"{user.name} <{user.email}>"
        items += (
            f'<li class="list-group-item">'
            f'<a href="/users/{user.id}/">{text}</a>'
            f'</li>'
        )
    content = f"""
    <h1>Пользователи каталога</h1>
    <ul class="list-group">{items}</ul>
    """
    return HttpResponse(page("TourCatalog — пользователи", content))


def user_detail(request, user_id):
    """Страница конкретного пользователя."""
    users_list = load_users("data/users.json")
    user = find_user_by_id(users_list, user_id)

    if user is None:
        content = """
        <h1 class="text-danger">Пользователь не найден</h1>
        <a href="/users/" class="btn btn-outline-secondary">
        ← к списку пользователей
        </a>
        """
        return HttpResponse(
            page("Пользователь не найден", content),
            status=404,
        )

    content = f"""
    <div class="card">
    <div class="card-body">
    <h5 class="card-title">{user.name}</h5>
    <p class="card-text"><strong>ID:</strong> {user.id}</p>
    <p class="card-text"><strong>Email:</strong> {user.email}</p>
    <a href="/users/" class="btn btn-outline-secondary">
    ← к списку пользователей
    </a>
    </div>
    </div>
    """
    return HttpResponse(
        page(user.name, content),
        status=200,
    )