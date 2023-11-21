from selenium import webdriver
from selenium.webdriver.common.by import By
import time
#import math


#def calc(x):
#    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

#    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
#    x = x_element.text
#    y = calc(x)
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None
    #answer = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    #robotCheckbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    #robotsRule = browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    #submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()