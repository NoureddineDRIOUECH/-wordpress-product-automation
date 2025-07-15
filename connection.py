
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def connection():
    with open('config.json') as f:
        config = json.load(f)
    
    username = config['username']
    password = config['password']
    url = config['url']
    headless = config['headless']

    firefox_options = Options()
    if headless:
        firefox_options.add_argument("--headless")
    
    driver = webdriver.Firefox(options=firefox_options)
    driver.get(url)
    
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "user_login")))
        element.send_keys(username + Keys.TAB + password + Keys.ENTER)
    except Exception as e:
        print(f"An error occurred during login: {e}")
        driver.quit()
        raise
        
    return driver