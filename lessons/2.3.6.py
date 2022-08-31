'''
Открыть страницу http://suninjuly.github.io/redirect_accept.html
Нажать на кнопку
Переключиться на новую вкладку
Пройти капчу для робота и получить число-ответ
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, '[class="trollface btn btn-primary"]')
    button.click()
    time.sleep(2)
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    time.sleep(1)
    x = int(browser.find_element(By.CSS_SELECTOR, '[id="input_value"]').text)
    func = math.log(abs(12*math.sin(x)))
    input_field = browser.find_element(By.CSS_SELECTOR, '[class="form-control"]')
    input_field.send_keys(func)
    button = browser.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]')
    button.click()
    print(browser.switch_to.alert.text)
    browser.switch_to.alert.accept()
    time.sleep(1)

except Exception as ex:
    print(ex)
finally:
    browser.close()
    browser.quit()
