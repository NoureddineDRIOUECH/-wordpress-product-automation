imageLink = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@id="set-post-thumbnail"]')))
imageLink.click()

cwd = os.getcwd()

# Assuming 'file_name' is the name of the file you want to upload
file_name = "appareil-photo-couleur-instantane-canon-zoemini-s2-blanc-perle-4519c007aa.jpg"

# Construct the absolute file path
abs_file_path = os.path.join("/home", "noureddinedriouech", "Downloads", "irisDataScraping", "productsImages", file_name)

file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
file_input.send_keys(abs_file_path)
time.sleep(5)

# Wait for the "Insert into post" button to be clickable and click it
imageLink = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@class="button media-button button-primary button-large media-button-select"]')))
imageLink.click()