import json
from createProduct import create_product
from connection import connection
from selenium.webdriver.support.wait import WebDriverWait
from fillingForm import get_add_page
with open('115-compact_data.json') as f:
    products_data = json.load(f)

driver = connection('admin', 'tv4GvG4sSfR84bJ@', 'https://test.wa7id.com/wp-admin')
driver.maximize_window()
get_add_page(driver)


for product_data in products_data:
    create_product(driver, product_data)
print("done!")
driver.close()
driver.quit()