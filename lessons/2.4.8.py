import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, 'price'), '100')
        )
    button = browser.find_element(By.ID, 'book')
    button.click()
    x = int(browser.find_element(By.ID, 'input_value').text)
    func = math.log(abs(12 * math.sin(x)))
    math_operation_field = browser.find_element(By.ID, 'answer')
    math_operation_field.send_keys(func)
    button = browser.find_element(By.ID, 'solve')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    alert_text = browser.switch_to.alert.text
    print(alert_text)
    browser.switch_to.alert.accept()


except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()

