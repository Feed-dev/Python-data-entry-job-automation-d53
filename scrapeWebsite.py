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
    properties = soup.select("div.property-card")

    data = []
    for property in properties:
        address = property.find("address", {"data-test": "property-card-addr"}).get_text(strip=True)
        price = property.find("span", {"data-test": "property-card-price"}).get_text(strip=True).replace("+", "").split("/")[0].strip()
        link = property.find("a", {"data-test": "property-card-link"})["href"]
        data.append({"address": address, "price": price, "link": link})

    return data


properties_data = scrape_zillow()
print(properties_data)
