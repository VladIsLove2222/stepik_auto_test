from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполняем обязательные поля
    # Поле First name
    first_name_input = browser.find_element(By.NAME, "firstname")
    first_name_input.send_keys("TestFirstName")

    # Поле Last name
    last_name_input = browser.find_element(By.NAME, "lastname")
    last_name_input.send_keys("TestLastName")

    # Поле Email
    email_input = browser.find_element(By.NAME, "email")
    email_input.send_keys("test@example.com")

    file_find = browser.find_element(By.ID, "file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '1.txt')           # добавляем к этому пути имя файла 
    file_find.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
