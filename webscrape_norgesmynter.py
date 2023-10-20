from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser

# Use configparser to keep username and password confidential

config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('credentials', 'username')
password = config.get('credentials', 'password')


def init_driver():
    driver = webdriver.Chrome()
    return driver

# Function to login on website, in order to access prices


# Array of urls with coins
urlArr = [

]

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

def scrape(url):
    driver.get(url)
    specifications = {}
    try:
        spec_container = driver.find_element_by_class_name('product-fields-one')
        field_text_elements = spec_container.find_elements_by_class_name('field-text')
        field_value_elements = spec_container.find_elements_by_class_name('field-value')

        field_text_elements = spec_container.find_elements_by_class_name('field-text')
        field_value_elements = spec_container.find_elements_by_class_name('field-value')

        for field_text, field_value in zip(field_text_elements, field_value_elements):
            key = field_text.text.strip()  
            value = field_value.text.strip()  
            specifications[key] = value  

    except NoSuchElementException as e:
        print("An element was not found. Error:", e)

    print(specifications)


if __name__ == "__main__":
    driver = init_driver()
    login(driver, username, password)
    scrape("https://norgesmynter.no/produkt/1-krone-1908-1917/")


driver.quit()
