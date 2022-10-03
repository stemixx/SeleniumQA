import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import math

browser = webdriver.Chrome()


def Foo(x):
    return math.log(abs(12 * math.sin(x_value)))


try:
    browser.get("https://suninjuly.github.io/math.html")
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x_value = int(x_element.text)
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(Foo(x_value))
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()
    answer = browser.switch_to.alert
    answer_text = answer.text
    browser.switch_to.alert.accept()
    print(answer_text)


except Exception as ex:
    print(ex)

finally:
    browser.close()
    browser.quit()
