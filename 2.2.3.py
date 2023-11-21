from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.ID, "num1")

    a = num1.text
    num2 = browser.find_element(By.ID, "num2")

    b = num2.text
    summ = str(str(int(a)+int(b)))
    print(summ)

    dropdown = Select(browser.find_element(By.TAG_NAME, "select"))

    dropdown.select_by_value(str(summ))
    submit = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()