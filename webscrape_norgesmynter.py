from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('credentials', 'username')
password = config.get('credentials', 'password')

def init_driver():
    driver = webdriver.Chrome()
    return driver

def login(driver, username, password):
    driver.get("https://norgesmynter.no/min-profil/")
    try:
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        submit_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "login"))
        )

        username_field.send_keys(username)
        password_field.send_keys(password)
        submit_button.click()

    except TimeoutException:
        print("Element not found on the page or took too long to load.")

if __name__ == "__main__":
    driver = init_driver()
    login(driver, username, password)


driver.quit()
