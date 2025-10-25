# 🗺️ TeamPelid

**TeamPelid** — это Django-бэкенд для работы с геоданными и карточками мест на карте Москвы.
Позволяет хранить, редактировать и выдавать информацию о достопримечательностях, парках, зданиях и других интересных точках через удобное REST-API и админку.

---

## 🌍 Онлайн-версия проекта

Проект уже задеплоен и доступен онлайн:
🔗 **[https://pavlowave.pythonanywhere.com/](https://pavlowave.pythonanywhere.com/)**

На сайте работает:
- Главная страница с интерактивной картой
- API эндпоинты (`home/ [name='home_page']`,`/places-geojson/`, `/places/<id>/`)
- Django-админка: [https://pavlowave.pythonanywhere.com/admin/](https://pavlowave.pythonanywhere.com/admin/)
  > При необходимости можно выдать доступ к админке для проверки прав администратора.

---

## 📋 Описание проекта

Реализовано:
- Django-админка для добавления и редактирования мест
- REST API с данными о локациях
- Возврат всех точек в формате **GeoJSON**
- Скрипт автоматической загрузки пачки JSON-файлов с описаниями мест
- Удобная структура хранения данных и изображений

---

## ⚙️ Технологии

- Python 3.10+
- Django 4.x
- Django REST Framework
- Pillow (для изображений)
- SQLite (по умолчанию)

---

## 📁 Структура проекта

```
TeamPelid/
├── config/                # настройки Django
│   ├── settings.py
│   └── urls.py
├── modules/
│   └── locations/         # приложение с моделями, сериализаторами и views
├── scripts/
│   └── load_places.py     # скрипт для пакетной загрузки JSON-файлов
├── media/places/          # изображения мест
├── places.json            # пример фикстуры
├── requirements.txt
└── manage.py
```

---

## 🧭 Быстрый старт (локально)

1. **Клонировать репозиторий**
   ```bash
   git clone https://github.com/pavlowave/TeamPelid.git
   cd TeamPelid
   ```

2. **Создать виртуальное окружение и установить зависимости**
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   pip install -r requirements.txt
   ```

3. **Применить миграции**
   ```bash
   python manage.py migrate
   ```

4. **Создать суперпользователя**
   ```bash
   python manage.py createsuperuser
   ```

5. **Запустить сервер**
   ```bash
   python manage.py runserver
   ```
   Приложение будет доступно по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📦 Загрузка данных из JSON-файлов

В проекте предусмотрен скрипт `scripts/load_places.py`, который автоматически добавляет в базу все места из набора JSON-файлов, расположенных в локальной папке.

### Пример структуры JSON-файла
```json
{
  "title": "Лужники",
  "description_short": "Главный стадион Москвы.",
  "description_long": "<p>Стадион Лужники — крупнейший спортивный комплекс Москвы...</p>",
  "coordinates": {"lat": 55.715765, "lng": 37.553924},
  "imgs": ["media/places/luzhniki_1.jpg"]
}
```

### Формат поддерживает пакетную загрузку
Можно загрузить сразу несколько JSON-файлов из папки, например:
```
data/
├── luzhniki.json
├── zaryadye.json
├── vdnh.json
```

### Запуск скрипта
```bash
python scripts/load_places.py data/
```
Скрипт автоматически:
- Прочитает все `.json` файлы в указанной директории
- Создаст соответствующие записи в базе данных
- Привяжет изображения (если пути корректны)

---

## 🧩 Основные URL-маршруты

| URL | Имя маршрута | Описание |
|:--------------------------|:-------------------|:------------------------------|
| `/admin/` | — | Панель администратора Django |
| `/` | `home_page` | Главная страница проекта |
| `/places-geojson/` | `places_geojson` | Возвращает все локации в формате GeoJSON |
| `/places/<int:place_id>/` | `place_detail` | Возвращает данные об одном месте (по ID) |

Примеры запросов:
```bash
curl http://127.0.0.1:8000/places-geojson/
curl http://127.0.0.1:8000/places/1/
```

---

## 🧠 Админка

Админ-панель доступна по адресу [https://pavlowave.pythonanywhere.com/admin/](https://pavlowave.pythonanywhere.com/admin/)
Если нужны права для просмотра — их можно выдать по запросу.

Возможности:
- Добавление новых мест вручную
- Загрузка изображений
- Просмотр и редактирование существующих записей

---

## 🔐 Переменные окружения (.env)

```
DEBUG=True
SECRET_KEY=уникальный_ключ
ALLOWED_HOSTS=127.0.0.1,localhost,pavlowave.pythonanywhere.com

```

---

## 📬 Контакты

Автор проекта — **Павел**
📧 GitHub: [pavlowave](https://github.com/pavlowave)
