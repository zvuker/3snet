# Тестовое задание — 3SNET Events Widget (Playwright + Python)

Репозиторий содержит пример автотеста для страницы: `https://dev.3snet.info/eventswidget/`.


## Покрытие теста

- Страница доступна и загружается.
- Кнопка «Сгенерировать превью» находится и нажимается.
- Поля ширины и высоты заполняются.
- После генерации появляется <iframe>.
- В поле с кодом появляется HTML с <iframe> и правильными width/height.
- Проверяются ошибки в консоли


## Требования

- Python 3.9+
- Playwright
- pytest


## Установка

```bash
# 1. Клонировать репозиторий
# git clone <https://github.com/zvuker/3snet>
# cd 3snet


# 2. Создать виртуальное окружение 
python -m venv .venv
# активация:
# Windows: .\.venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate


# 3. Установить зависимости
pip install -r requirements.txt


# 4. Установить браузеры Playwright
playwright install


# 5. Запуск теста:
pytest -v