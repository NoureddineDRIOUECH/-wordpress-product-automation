from fillingForm import *
def create_product(driver, product_data):
    # Extract product data
    name = product_data['name']
    regular_price = product_data['regular_price']
    sale_price = product_data['sale_price']
    description = product_data['description']
    images = product_data['images']

    set_title(driver,name)
    if(description != None):
        set_description(driver,description)

    # Upload product image
    file_name = os.path.basename(images[0])

    # Construct the absolute file path
    abs_file_path = os.path.join("/home", "noureddinedriouech", "Downloads", "irisDataScraping", "productsImages", file_name)
    upload_product_image(driver, abs_file_path)
    if(regular_price == None ):
        sale_price_float = float(sale_price.replace(',', '.'))  # Remove comma and convert to float
        regular_price = round(sale_price_float / (1 - 0.10))
    # Set product prices
    set_product_prices(driver, regular_price, sale_price)

    # Set tax status and class
    set_tax_status(driver)
    set_tax_class(driver)

    # Publish product
    publish_product(driver)