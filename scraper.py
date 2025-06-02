import requests
from bs4 import BeautifulSoup

def scrape_mercadolibre(query, limit=10):
    results = []
    query = query.replace(" ", "-")
    url = f"https://listado.mercadolibre.com.ar/{query}"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.select(".ui-search-layout__item")[:limit]

    for item in items:
        title = item.select_one("h2.ui-search-item__title")
        price = item.select_one(".ui-search-price__part")
        link = item.select_one("a.ui-search-link")

        if title and price and link:
            results.append({
                "titulo": title.get_text(strip=True),
                "precio": price.get_text(strip=True),
                "url": link["href"]
            })

    return results
