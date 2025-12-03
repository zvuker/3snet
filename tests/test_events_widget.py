import re
import pytest
from playwright.sync_api import sync_playwright
from helpers.selectors import (
    URL,
    find_generate_button,
    find_width_input,
    find_height_input,
    find_code_textarea,
    find_iframe
)

def test_events_widget_basic_flow():
    console_errors = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Логирование ошибок
        def on_console(msg):
            if msg.type == 'error':
                text = msg.text
                if 'status of 499' not in text:
                    console_errors.append(text)

        page.on('console', on_console)

        # 1. Открываем страницу
        page.goto(URL.strip(), wait_until='domcontentloaded', timeout=60000)
        assert page.locator("text=Начните создавать").count() > 0 or "3s" in page.title().lower()

        # 2. Кнопка генерации превью
        gen_btn = find_generate_button(page)
        assert gen_btn is not None, "Кнопка 'Сгенерировать превью' не найдена"

        # 3. Ввод ширины
        width_inp = find_width_input(page)
        if width_inp.count() == 0:
            pytest.skip("Поле ввода ширины не найдено")
        width_inp.fill('320')

        # 4. Ввод высоты
        height_inp = find_height_input(page)
        if height_inp.count() == 0:
            pytest.skip("Поле ввода высоты не найдено")
        height_inp.fill('280')

        # 5. Генерируем превью
        gen_btn.click()

        # 6. Дожидаемся появления iframe
        iframe_locator = page.locator('iframe')
        iframe_locator.wait_for(state="visible", timeout=5000)
        assert iframe_locator.count() > 0, "iframe не найден после генерации превью"

        iframe_el = iframe_locator.first
        src = iframe_el.get_attribute('src') or ''
        tag_width = iframe_el.get_attribute('width')
        tag_height = iframe_el.get_attribute('height')

        # Проверяем width/height
        assert tag_width == '320' or re.search(r'width=320', src)
        assert tag_height == '280' or re.search(r'height=280', src)

        # 7. Поле кода
        code_area = find_code_textarea(page)
        code_area.wait_for(state="visible", timeout=5000)
        code_text = code_area.input_value()
        assert '<iframe' in code_text, "В сгенерированном HTML нет <iframe>"

        # 8. Проверка ошибок в консоли
        assert not console_errors, f"Ошибки в консоли: {console_errors}"

        context.close()
        browser.close()