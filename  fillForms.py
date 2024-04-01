from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from scrapeWebsite import scrape_zillow


def fill_google_form(data):
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc5UQiiGO11tUTnDYB1NcuQJB9WQIzDWfgFjwbYVoTsY0MUng/viewform?usp=sf_link"

    # Setup Chrome and open the form
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    for entry in data:
        driver.get(form_url)
        time.sleep(2)  # Adjust based on your internet speed

        # Fill the address
        address_field = driver.find_element(By.XPATH,
                                            "/html/body/div/div[3]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input")
        address_field.send_keys(entry["address"])

        # Fill the price
        price_field = driver.find_element(By.XPATH,
                                          "/html/body/div/div[3]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input")
        price_field.send_keys(entry["price"])

        # Fill the link
        link_field = driver.find_element(By.XPATH,
                                         "/html/body/div/div[3]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input")
        link_field.send_keys(entry["link"])

        # Click the submit button
        submit_button = driver.find_element(By.XPATH, "/html/body/div/div[3]/form/div[2]/div/div[3]/div[1]/div[1]/div")
        submit_button.click()

        time.sleep(1)  # Wait a bit for form to submit

    # Close the browser once all forms are submitted
    driver.quit()


# Assuming properties_data is the list of dictionaries containing the scraped data
properties_data = scrape_zillow()  # Make sure to have this function from the previous step
fill_google_form(properties_data)

