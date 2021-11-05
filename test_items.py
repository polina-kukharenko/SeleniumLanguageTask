import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_basket_button_is_exist(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)  # пауза, чтобы посмотреть на страницу и найти нужную кнопку глазами, 30сек - это много:)

    # в случае, если кнопка не будет найдена, выпадет исключение TimeoutException и сообщение "Button is not exist"
    # можно использовать инструкцию browser.find_element_by* но мы так же не дойдём до assert в случае отсутствия кнопки
    # однако, с исключением NoSuchElementException не получим осмысленного сообщения в тест-отчете
    basket_button = WebDriverWait(browser, 3).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[type="submit"].btn-add-to-basket')),
        "Button is not exist"
    )

    # в задаче требуется assert, но до этой строчки дойдём только если кнопка будет найдена
    assert basket_button, "Assert message: Button is not exist"
