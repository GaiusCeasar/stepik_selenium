from os import environ
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By
import time
import math

# link = f"http://selenium1py.pythonanywhere.com/{language}/"
# @pytest.mark.parametrize('language', ["ru", "en-gb"])

from dotenvy import load_env, read_file

load_env(read_file('.env'))


@pytest.mark.parametrize('number', ["236895",
                                  "236896",
                                  "236897",
                                  "236898",
                                  "236899",
                                  "236903",
                                  "236904",
                                  "236905"])
def test_guest_should_see_login_link(browser, number):
    try:
        link = f"https://stepik.org/lesson/{number}/step/1"
        login = environ.get('LOGIN')
        password = environ.get('PASS')
        browser.get(link)
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "ember33"))
        )
        element.click()
        browser.find_element(By.ID, "id_login_email").send_keys(login)
        browser.find_element(By.ID, "id_login_password").send_keys(password)
        browser.find_element(By.CLASS_NAME, "sign-form__btn").click()
        browser.implicity_wait(10)
        input = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "textarea"))
        )
        answer = math.log(int(time.time()))
        print(answer)
        # input.click()
        input.send_keys(answer)
        # time.sleep(5)
        sunm = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "submit-submission"))
        )
        sunm.click()
        priverka = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))).text
        assert priverka == "Correct!"
    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(10)
        # закрываем браузер после всех манипуляций
        browser.quit()
