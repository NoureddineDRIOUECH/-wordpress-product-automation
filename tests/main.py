from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from connection import connection
import os
import time
import json

with open('115-compact_data.json') as f:
    products_data = json.load(f)





driver = connection('admin','tv4GvG4sSfR84bJ@','https://test.wa7id.com/wp-admin')
wait = WebDriverWait(driver, 5)

driver.maximize_window()

WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@href='edit.php?post_type=product']"))).click()
WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//a[@class='page-title-action']"))).click()


for product in products_data:
    # Extract product data
    name = product['name']
    regular_price = product['regular_price']
    sale_price = product['sale_price']
    description = product['description']
    images = product['images']

    title = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "title")))
    driver.execute_script("arguments[0].scrollIntoView()",title)
    title.send_keys(name)


    time.sleep(1)
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[id^='content_ifr']"))
    )
    driver.switch_to.frame(iframe)
    p_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    driver.execute_script(f"arguments[0].textContent = '{description.replace('\'', '\\\'').replace('\n', '\\n')}';", p_element)
    driver.switch_to.default_content()






    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="set-post-thumbnail"]'))).click()


    # Assuming 'file_name' is the name of the file you want to upload
    file_name = os.path.basename(images[0])

    # Construct the absolute file path
    abs_file_path = os.path.join("/home", "noureddinedriouech", "Downloads", "irisDataScraping", "productsImages", file_name)
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_input.send_keys(abs_file_path)
    time.sleep(2)

    # Wait for the "Insert into post" button to be clickable and click it
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button media-button button-primary button-large media-button-select"]'))).click()





    prices = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "_regular_price")))
    driver.execute_script('window.scrollTo(0,550)')
    prices.send_keys(str(regular_price) + Keys.TAB + str(sale_price))

    dropdown = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "_tax_status")))
    select = Select(dropdown)
    driver.execute_script('window.scrollTo(0,650)')
    select.select_by_value("none")
    dropdown = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "_tax_class")))
    select = Select(dropdown)
    select.select_by_value("reduced-rate")
    time.sleep(1)

    driver.execute_script('window.scrollTo(0,0)')
    time.sleep(1)
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"publish"))).click()
    time.sleep(2)


    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//a[@class='page-title-action']"))).click()
    time.sleep(2)
    
print("done!")
driver.close()
driver.quit()