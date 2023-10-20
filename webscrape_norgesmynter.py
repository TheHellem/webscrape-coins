from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
from bs4 import BeautifulSoup

# Use configparser to keep username and password confidential

config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('credentials', 'username')
password = config.get('credentials', 'password')

def init_driver():
    driver = webdriver.Chrome()
    return driver

# Array of urls with coins
urlArr = [

]

# Function to login on website, in order to access prices
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

def scrape(url, driver):
    driver.get(url)
    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        
        title_element = soup.find('div', class_='h1-content').find('h1')
        title_text = title_element.text

        specifications = {}
        spec_container = soup.find('div', class_='product-fields-one')
        field_text_elements = spec_container.find_all('div', class_='field-text')
        field_value_elements = spec_container.find_all('div', class_='field-value')
        
        for field_text, field_value in zip(field_text_elements, field_value_elements):
            key = field_text.text.strip()
            value = field_value.text.strip()
            specifications[key] = value

        table_data = []
        table = soup.find('table', class_='col-md-12')
        rows = table.find('tbody').find_all('tr')
        
        for row in rows:
            columns = row.find_all('td')
            values = [column.get_text(strip=True) for column in columns]
            table_data.append(values)

        print(title_text)
        print(specifications)
        for row_data in table_data:
            print(row_data)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    driver = init_driver()
    login(driver, username, password)
    
    urls = [
        "https://norgesmynter.no/produkt/1-krone-1908-1917/",
        # Add more URLs if needed
    ]
    
    for url in urls:
        scrape(url, driver)

    driver.quit()