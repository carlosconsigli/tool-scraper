import requests
from bs4 import BeautifulSoup

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def scrape_page(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'lxml')

        # Heurística básica
        title = soup.find("title").text.strip() if soup.find("title") else "Título no encontrado"
        
        price_candidates = soup.find_all(string=lambda t: "$" in t or "USD" in t or "€" in t)
        prices = [p.strip() for p in price_candidates if len(p.strip()) < 30][:3]
        
        return {
            "title": title,
            "prices": prices,
            "success": True
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
