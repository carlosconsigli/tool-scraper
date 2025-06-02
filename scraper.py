import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_mercadolibre(query):
    try:
        # Convertimos la consulta en formato de URL
        query_encoded = urllib.parse.quote(query)
        url = f"https://www.mercadolibre.com.ar/jm/search?as_word={query_encoded}"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Error HTTP {response.status_code}")
            return []

        soup = BeautifulSoup(response.text, "html.parser")

        items = soup.select("li.ui-search-layout__item")

        results = []
        for item in items[:10]:
            title = item.select_one("h2.ui-search-item__title")
            price_integer = item.select_one("span.price-tag-fraction")
            link = item.select_one("a.ui-search-link")

            if title and price_integer and link:
                results.append({
                    "title": title.get_text(strip=True),
                    "price": price_integer.get_text(strip=True),
                    "url": link["href"]
                })

        return results

    except Exception as e:
        print("Error durante el scraping:", e)
        return []