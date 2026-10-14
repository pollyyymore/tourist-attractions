# TourCatalog — каталог туристических мест

## Назначение

TourCatalog — приложение для ведения каталога туристических мест
и формирования личного списка избранного для посещения.
Консольная версия (ПР3) дополнена веб-интерфейсом на Django (ПР5).

Приложение позволяет:

- просматривать места в браузере;
- просматривать информацию о конкретном месте;
- просматривать пользователей каталога;
- просматривать избранное;
- получать доступ к данным через веб-интерфейс;
- сохранять возможность работы консольной версии.

## Используемые технологии

- Python 3;
- Django 5.2 — веб-фреймворк;
- HTML, CSS, Bootstrap 5.3 — вёрстка и оформление;
- pytest — автоматизированные тесты;
- flake8 — проверка качества кода.

## Предметная область

Основные сущности:

- **Place** — туристическое место (id, name, region, category, description, rating);
- **User** — пользователь каталога (id, name, email);
- **Favorite** — запись избранного (id, place, user, visit_date, is_cancelled).

Одно место не может иметь двух активных записей избранного на одну дату.
Отменённая запись не блокирует место.

## Страницы веб-интерфейса

- `/` — главная страница (view `index`);
- `/places/` — список мест (view `places`);
- `/places/<int:place_id>/` — страница места (view `place_detail`);
- `/users/` — список пользователей (view `users`);
- `/users/<int:user_id>/` — страница пользователя (view `user_detail`);
- `/favorites/` — список избранного (view `favorites`);
- `/favorites/<int:favorite_id>/` — страница записи (view `favorite_detail`).

При обращении к несуществующему идентификатору возвращается код 404.

## Основные операции

### Используется в веб-интерфейсе (ПР5)

- просмотр списка мест;
- просмотр информации о месте;
- просмотр списка пользователей;
- просмотр информации о пользователе;
- просмотр списка избранного;
- просмотр информации о записи.

### Отложено до следующих работ

- добавление, редактирование, отмена;
- поиск и фильтрация через формы;
- POST-запросы.

## Хранение данных

Данные приложения хранятся в JSON-файлах:

- `data/places.json`;
- `data/users.json`;
- `data/favorites.json`.

При загрузке данные из JSON преобразуются в объекты `Place`, `User`,
`Favorite`. Для связи записи с местом и пользователем в `favorites.json`
используются их идентификаторы `place_id` и `user_id`.

## Структура проекта

```text
tour_catalog/
├── README.md
├── requirements.txt
├── conftest.py
├── manage.py
├── main.py
├── storage.py
├── utils.py
├── tourcatalog/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── homepage/
│   ├── views.py      (page, index, page_not_found)
│   └── urls.py
├── places/
│   ├── views.py      (places, place_detail)
│   └── urls.py
├── users/
│   ├── views.py      (users, user_detail)
│   └── urls.py
├── favorites/
│   ├── views.py      (favorites, favorite_detail)
│   └── urls.py
├── models/
│   ├── places.py
│   ├── users.py
│   └── favorites.py
├── data/
│   ├── places.json
│   ├── users.json
│   └── favorites.json
└── tests/
    ├── test_places.py
    ├── test_users.py
    └── test_favorites.py
```

## Назначение модулей

### `main.py`

Консольная версия приложения (сохранена с ПР3).

### `tourcatalog/`

Пакет настроек Django-проекта: `settings.py`, `urls.py`, `asgi.py`, `wsgi.py`.

### `homepage/`

Django-приложение, отвечающее за главную страницу и общий каркас:

- `views.py` — `page()` (общий HTML-каркас), `index()`, `page_not_found()`;
- `urls.py` — маршрут главной страницы.

### `places/`

Django-приложение, отвечающее за места:

- `views.py` — `places()`, `place_detail()`;
- `urls.py` — маршруты приложения;
- `models.py` — Django-модели (заполняется на следующих работах).

### `users/`

Django-приложение для пользователей:

- `views.py` — `users()`, `user_detail()`;
- `urls.py` — маршруты приложения.

### `favorites/`

Django-приложение для избранного:

- `views.py` — `favorites()`, `favorite_detail()`;
- `urls.py` — маршруты приложения.

### `models/`

Классы предметной области и функции работы с ними (пакет ПР3).

### `storage.py`

Загрузка и сохранение данных: `JSON ↔ объекты Python`.

### `utils.py`

Вспомогательные функции ввода.

### `tests/`

Автоматизированные тесты проекта.

## Запуск приложения

Веб-версия (Django):

```text
python manage.py runserver
```

Проверить все ли в порядке:

```text
python manage.py check
```

Открыть `http://127.0.0.1:8000/`.

Консольная версия:

```text
python main.py
```

## Тестирование

```text
pytest -v
```

## Проверка качества кода

```text
flake8
```

## Зависимости

- `Django==5.2.*` — веб-фреймворк;
- `pytest` — автоматизированные тесты;
- `flake8` — проверка качества кода.

## Git

Исходный код хранится в Git-репозитории. Коммиты ПР5 имеют метку `PR5:`.

## Текущее состояние и план развития

Реализовано (ПР5):

- Django-проект и четыре Django-приложения (`homepage`, `places`, `users`, `favorites`);
- маршрутизация URL двух уровней;
- view-функции и страницы;
- отображение объектов `Place`, `User`, `Favorite` в HTML;
- обработка ошибки 404;
- навигация между страницами;
- Bootstrap 5.3 через CDN.

Планируется:

- перенос `Place`, `User`, `Favorite` в Django ORM;
- подключение базы данных;
- переход на `templates/` и `render()`;
- формы создания и отмены записей;
- API и дальнейшее развитие.
