import requests
from bs4 import BeautifulSoup
import urllib.parse

def scrape_mercadolibre(query):
    try:
        query_encoded = urllib.parse.quote(query)
        url = f"https://listado.mercadolibre.com.ar/{query_encoded}"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/122.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.select("li.ui-search-layout__item")

        results = []
        for item in items[:10]:  # limitamos a 10 resultados
            title = item.select_one("h2.ui-search-item__title")
            price = item.select_one("span.price-tag-fraction")
            link = item.select_one("a.ui-search-link")

            if title and price and link:
                results.append({
                    "title": title.text.strip(),
                    "price": price.text.strip(),
                    "url": link["href"].split("#")[0]  # eliminamos el fragmento de URL
                })

        if not results:
            return [{"error": "No se encontraron productos. Puede haber cambios en el sitio web."}]
        return results

    except Exception as e:
        return [{"error": str(e)}]
