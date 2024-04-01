from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from scrapeWebsite import scrape_zillow


def fill_google_form(data):
    form_url = "https://forms.gle/LkgftVszNN6Wbj1j6"

    # Setup Chrome and open the form
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for entry in data:
        driver.get(form_url)
        time.sleep(2)  # Adjust based on your internet speed

        # Find and fill the address field
        address_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address_field.send_keys(entry["address"])

        # Find and fill the price field
        price_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_field.send_keys(entry["price"])

        # Find and fill the link field
        link_field = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_field.send_keys(entry["link"])

        # Submit the form
        submit_button = driver.find_element(by=By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
        submit_button.click()

        # Wait a second before submitting the next form
        time.sleep(1)

    # Close the browser after submitting all forms
    driver.quit()


# Assuming properties_data is the list of dictionaries containing the scraped data
properties_data = scrape_zillow()  # Ensure this function is defined as above
fill_google_form(properties_data)
