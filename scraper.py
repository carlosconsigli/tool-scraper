import requests
from bs4 import BeautifulSoup

def scrape_mercadolibre(query):
    try:
        # Convertir el texto de búsqueda en formato URL amigable
        query = query.replace(' ', '+')
        url = f"https://listado.mercadolibre.com.ar/{query}"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/113.0.0.0 Safari/537.36"
            )
        }

        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.select('li.ui-search-layout__item')

        results = []
        for item in items[:10]:  # Solo los primeros 10
            title_elem = item.select_one('h2.ui-search-item__title')
            price_elem = item.select_one('span.price-tag-fraction')
            link_elem = item.select_one('a.ui-search-link')

            if title_elem and price_elem and link_elem:
                results.append({
                    "title": title_elem.text.strip(),
                    "price": price_elem.text.strip(),
                    "url": link_elem['href']
                })

        return results

    except Exception as e:
        print(f"Error durante el scraping: {e}")
        return []

