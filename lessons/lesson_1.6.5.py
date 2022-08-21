'''
Найти на странице http://suninjuly.github.io/find_link_text текст ссылки, зашифрованный формулой:
str(math.ceil(math.pow(math.pi, math.e)*10000))
Перейти по найденной ссылке и заполнить форму. Нажать кнопку и получить код
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


finding_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome('E:\!install\chromedriver.exe')
    browser.get(link)

    find_hidden_link = browser.find_element(By.PARTIAL_LINK_TEXT, finding_text)
    find_hidden_link.click()
    input_firstname = browser.find_element(By.TAG_NAME, 'input')
    input_firstname.send_keys('Ivan')
    input_surname = browser.find_element(By.NAME, 'last_name')
    input_surname.send_keys('Petrov')
    input_city = browser.find_element(By.CLASS_NAME, 'city')
    input_city.send_keys('Vologda')
    input_country = browser.find_element(By.ID, 'country')
    input_country.send_keys('Russia')
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

