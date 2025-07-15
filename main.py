import json
from createProduct import create_product
from connection import connection
from fillingForm import get_add_page
with open('151-onduleur-off-line_data.json') as f:
    products_data = json.load(f)

driver = connection('admin', 'yout ubfo,' 'Your Innfo')
driver.maximize_window()
get_add_page(driver)


for product_data in products_data:
    create_product(driver, product_data)
print("done!")
driver.close()
driver.quit()
