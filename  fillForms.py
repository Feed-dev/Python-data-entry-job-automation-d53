from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def fill_google_form(data):
    form_url = "https://docs.google.com/forms/d/e/1FAIpQLSc5UQiiGO11tUTnDYB1NcuQJB9WQIzDWfgFjwbYVoTsY0MUng/viewform?usp=sf_link"
    driver = webdriver.Chrome()  # or use webdriver.Firefox(), etc.

    for entry in data:
        driver.get(form_url)
        time.sleep(2)

        address_field = driver.find_element_by_xpath("Your Xpath for Address")
        price_field = driver.find_element_by_xpath("Your Xpath for Price")
        link_field = driver.find_element_by_xpath("Your Xpath for Link")

        address_field.send_keys(entry["address"])
        price_field.send_keys(entry["price"])
        link_field.send_keys(entry["link"])

        submit_button = driver.find_element_by_xpath("Your Xpath for Submit Button")
        submit_button.click()

        time.sleep(1)  # Wait for submission to complete

    driver.quit()


fill_google_form(properties_data)
