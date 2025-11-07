from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select



try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    a_element = browser.find_element(By.ID, "num1")
    a = int(a_element.text)
    b_element = browser.find_element(By.ID, "num2")
    b = int(b_element.text)
    x = str(a + b)
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_visible_text(x) 
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

