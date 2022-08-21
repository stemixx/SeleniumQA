'''
На странице http://suninjuly.github.io/find_xpath_form заполнить форму регистрации.
Нажать кнопку Submit, получить код
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome('E:\!install\chromedriver.exe')
    browser.get(link)

    input_name = browser.find_element(By.XPATH, "//input[@name='first_name']")
    input_name.send_keys('Ivan')
    input_surname = browser.find_element(By.XPATH, "//input[@name='last_name']")
    input_surname.send_keys('Petrov')
    input_city = browser.find_element(By.XPATH, "//input[@class='form-control city']")
    input_city.send_keys('Vologda')
    input_country = browser.find_element(By.XPATH, "//input[@id='country']")
    input_country.send_keys('Russia')
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

