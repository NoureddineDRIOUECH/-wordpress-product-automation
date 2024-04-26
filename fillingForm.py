import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Constants
WAIT_TIMEOUT = 10
REGULAR_PRICE_INPUT_ID = "_regular_price"
SALE_PRICE_INPUT_ID = "_sale_price"
TAX_STATUS_SELECT_ID = "_tax_status"
TAX_CLASS_SELECT_ID = "_tax_class"
PUBLISH_BUTTON_ID = "publish"

def upload_product_image(driver, abs_file_path):
    WebDriverWait(driver,WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, '//a[@id="set-post-thumbnail"]'))).click()
    file_input = WebDriverWait(driver,WAIT_TIMEOUT).until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(abs_file_path)
    time.sleep(2)
    WebDriverWait(driver,WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button media-button button-primary button-large media-button-select"]'))).click()

def set_product_prices(driver, regular_price, sale_price):
    driver.execute_script('window.scrollTo(0,550)')
    prices = WebDriverWait(driver,WAIT_TIMEOUT).until(EC.presence_of_element_located((By.ID, REGULAR_PRICE_INPUT_ID)))
    prices.send_keys(str(regular_price) + Keys.TAB + str(sale_price))

def set_tax_status(driver):
    dropdown = WebDriverWait(driver,WAIT_TIMEOUT).until(EC.presence_of_element_located((By.ID, TAX_STATUS_SELECT_ID)))
    select = Select(dropdown)
    driver.execute_script('window.scrollTo(0,650)')
    select.select_by_value("none")

def set_tax_class(driver):
    dropdown = WebDriverWait(driver,WAIT_TIMEOUT).until(EC.presence_of_element_located((By.ID, TAX_CLASS_SELECT_ID)))
    select = Select(dropdown)
    select.select_by_value("reduced-rate")

def publish_product(driver):
    driver.execute_script('window.scrollTo(0,0)')
    time.sleep(1)
    WebDriverWait(driver,WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.ID,PUBLISH_BUTTON_ID))).click()
    time.sleep(2)
    WebDriverWait(driver,WAIT_TIMEOUT).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='page-title-action']"))).click()

def set_title(driver, name):
    title = WebDriverWait(driver,WAIT_TIMEOUT).until(EC.presence_of_element_located((By.ID, "title")))
    driver.execute_script("arguments[0].scrollIntoView()",title)
    title.send_keys(name)


def set_description(driver, description):
    iframe = WebDriverWait(driver, WAIT_TIMEOUT).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[id^='content_ifr']"))
    )
    driver.switch_to.frame(iframe)
    p_element = WebDriverWait(driver, WAIT_TIMEOUT).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    driver.execute_script(f"arguments[0].textContent = '{description.replace('\'', '\\\'').replace('\n', '\\n')}';", p_element)
    driver.switch_to.default_content()

def get_add_page(driver):
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='edit.php?post_type=product']"))).click()
    WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='page-title-action']"))).click()
