from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import configparser
from bs4 import BeautifulSoup
import json

# Use configparser to keep username and password confidential

config = configparser.ConfigParser()
config.read('config.ini')

username = config.get('credentials', 'username')
password = config.get('credentials', 'password')

def init_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    return driver

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

def find_next_link(url, key_class, driver):
    try:
        driver.get(url)
        driver.implicitly_wait(0.5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        coin_type_container = soup.find('div', class_=key_class)
        coin_type_links = coin_type_container.find_all('a')
        urls = [link['href'] for link in coin_type_links]
    except Exception as e:
        print(f"An error occurred while processing URL {url}: {str(e)}")
        urls = []
    return urls

# It has to be a better way to do this, but I guess it works
def make_url_list (url, driver):
    coin_types_urls = find_next_link(url, "mynttype", driver)
    coin_edition_urls = []
    for url in coin_types_urls:
        coin_editions = find_next_link(url, "mynttype", driver)
        for url in coin_editions:
            coin_edition = find_next_link(url, "middleboxListing", driver)
            coin_edition_urls.append(coin_edition)
    return coin_edition_urls


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

        year_data = {}
        for row in rows:
            columns = row.find_all('td')
            values = [column.get_text(strip=True) for column in columns]
            year = values[1]  # Assuming the year is in the second column
            year_data[year] = {
                'title': title_text,
                'specifications': specifications,
                'Value': values[0],
                'Opplag': values[2],
                'Kv. 0': values[4],
                'Kv. 0/01': values[5],
                'Kv. 01': values[6],
                'Kv. 1+': values[7],
                'Kv. 1': values[8],
                'Kv. 1-': values[9],
                'Spesifikasjon': values[10]
            }

        return year_data

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    driver = init_driver()
    login(driver, username, password)
    
    nested_urls = make_url_list('https://norgesmynter.no/myntkatalogen/', driver)
    urls = [url for sublist in nested_urls for url in sublist]
   
    for url in urls:
        json_object = json.dumps(scrape(url, driver), indent=4)
        with open("norwegian_coins.json", "a") as outfile:  # Use "a" for append mode
            outfile.write(json_object)
            outfile.write("\n")  # Add a newline to separate JSON objects
        

    driver.quit()