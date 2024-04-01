import requests
from bs4 import BeautifulSoup


def scrape_zillow():
    url = "https://appbrewery.github.io/Zillow-Clone/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    # Create a list of all the links on the page using a CSS Selector
    all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
    # Python list comprehension (covered in Day 26)
    all_links = [link["href"] for link in all_link_elements]
    print(f"There are {len(all_links)} links to individual listings in total: \n")

    # Create a list of all the addresses on the page using a CSS Selector
    # Remove newlines \n, pipe symbols |, and whitespaces to clean up the address data
    all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
    all_addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address_elements]
    print(f"\n After having been cleaned up, the {len(all_addresses)} addresses now look like this: \n")

    # Create a list of all the prices on the page using a CSS Selector
    # Get a clean dollar price and strip off any "+" symbols and "per month" /mo abbreviation
    all_price_elements = soup.select(".PropertyCardWrapper span")
    all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if
                  "$" in price.text]
    print(f"\n After having been cleaned up, the {len(all_prices)} prices now look like this: \n")

    return [{"address": address, "price": price, "link": link} for address, price, link in
            zip(all_addresses, all_prices, all_links)]


properties_data = scrape_zillow()
print(properties_data)
