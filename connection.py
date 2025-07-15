
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
def connection(username, password , url):
    # Set up Firefox options
    # firefox_options = Options()
    # firefox_options.add_argument("--headless")  # Runs Firefox in headless mode
    driver = webdriver.Firefox()
    driver.get(url)
    element = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID, "user_login")))
    element.send_keys(username+ Keys.TAB + password + Keys.ENTER)
    return driver