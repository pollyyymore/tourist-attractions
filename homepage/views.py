"""View-функции приложения homepage + общий каркас страниц."""
from django.http import HttpResponse


def page(title: str, content: str) -> str:
    """Собрать HTML-документ с общим каркасом (Bootstrap + навигация)."""
    bootstrap = (
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3"
        "/dist/css/bootstrap.min.css"
    )
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="{bootstrap}">
</head>
<body>
<nav class="nav">
<a class="nav-link" href="/">Главная</a>
<a class="nav-link" href="/places/">Места</a>
<a class="nav-link" href="/users/">Пользователи</a>
<a class="nav-link" href="/favorites/">Избранное</a>
</nav>
<main class="container">{content}</main>
</body>
</html>"""


def index(request):
    """Главная страница каталога."""
    content = """
    <h1 class="display-4">TourCatalog</h1>
    <p class="lead">Каталог туристических мест.</p>
    <p>Основные разделы:</p>
    <a href="/places/" class="btn btn-primary me-2">Места</a>
    <a href="/users/" class="btn btn-success me-2">Пользователи</a>
    <a href="/favorites/" class="btn btn-secondary">Избранное</a>
    """
    return HttpResponse(page("TourCatalog", content))


def page_not_found(request, exception):
    """Собственная страница ошибки 404."""
    content = """
    <h1 class="text-danger">404 — страница не найдена</h1>
    <p>Проверьте адрес или вернитесь на главную.</p>
    <a href="/" class="btn btn-primary">На главную</a>
    """
    return HttpResponse(
        page("404 — страница не найдена", content),
        status=404,
    )