import json
from createProduct import create_product
from connection import connection
from fillingForm import get_add_page

def main():
    with open('151-onduleur-off-line_data.json') as f:
        products_data = json.load(f)

    driver = connection()
    driver.maximize_window()
    get_add_page(driver)

    for product_data in products_data:
        try:
            create_product(driver, product_data)
        except Exception as e:
            print(f"An error occurred while creating product {product_data.get('name')}: {e}")
            continue

    print("Done!")
    driver.quit()

if __name__ == "__main__":
    main()
