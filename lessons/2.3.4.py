'''
Открыть страницу http://suninjuly.github.io/alert_accept.html
Нажать на кнопку
Принять confirm
На новой странице решить капчу для роботов, чтобы получить число с ответом
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    button.click()
    time.sleep(1)
    browser.switch_to.alert.accept()
    time.sleep(1)
    x = int(browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text)
    func = math.log(abs(12*math.sin(x)))
    input_field = browser.find_element(By.CSS_SELECTOR, '[type="text"]')
    input_field.send_keys(func)
    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()
    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()
    time.sleep(2)

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
