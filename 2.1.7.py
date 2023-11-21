from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    treasure = x_element.get_attribute("valuex")
    y = calc(treasure)

    answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
