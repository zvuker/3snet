from playwright.sync_api import Page

URL = "https://dev.3snet.info/eventswidget/"

def find_generate_button(page: Page):
    return page.locator("button:has-text('Сгенерировать превью')").first

def find_width_input(page: Page):
    width_input = page.locator("input[name='width']")
    width_input.wait_for(state="visible", timeout=5000)
    return width_input.first

def find_height_input(page: Page):
    height_input = page.locator("input[name='height']")
    height_input.wait_for(state="visible", timeout=5000)
    return height_input.first

def find_code_textarea(page: Page):
    area = page.locator("//textarea[@id='code']")
    area.wait_for(state="visible", timeout=5000)
    return area.first

def find_iframe(page: Page):
    frame = page.locator("//div[@class='sport-name event-activity-name' and text()='Декабрь 2025']")
    frame.wait_for(state="visible", timeout=5000)
    return frame.first
