import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium.webdriver.common.by import By


# link = f"http://selenium1py.pythonanywhere.com/{language}/"
# @pytest.mark.parametrize('language', ["ru", "en-gb"])

def test_guest_should_see_login_link(browser):
    try:
        link = "https://stepik.org/lesson/236895/step/1"
        browser.get(link)
        time.sleep(5)
        #browser.find_element(By.ID, "ember33")
        login = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "ember33")))


    finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(3)
        # закрываем браузер после всех манипуляций
        browser.quit()
