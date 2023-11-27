from os import environ
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By


# link = f"http://selenium1py.pythonanywhere.com/{language}/"
# @pytest.mark.parametrize('language', ["ru", "en-gb"])

from dotenvy import load_env, read_file

load_env(read_file('.env'))
def test_guest_should_see_login_link(browser):
    try:
        link = "https://stepik.org/lesson/236895/step/1"
        login = environ.get('LOGIN')
        password = environ.get('PASS')
        browser.get(link)
        element = WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.ID, "ember33"))
        )
        element.click()
        browser.find_element(By.ID, "id_login_email").send_keys(login)
        browser.find_element(By.ID, "id_login_password").send_keys(password)
        browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
