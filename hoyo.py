import requests
from bs4 import BeautifulSoup

class PravdaNewsParser:
    def __init__(self, url="https://www.pravda.com.ua/"):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
        }

    def fetch_page(self):
        try:
            response = requests.get(self.url, headers=self.headers)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Помилка при завантаженні сторінки: {e}")
            return None

    def parse_news_titles(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        titles = []

        # Заголовки новин на головній сторінці (приклад селектора)
        news_blocks = soup.select('.article__title, .top-news__title')

        for block in news_blocks:
            title = block.get_text(strip=True)
            if title:
                titles.append(title)

        return titles

    def run(self):
        html = self.fetch_page()
        if html:
            titles = self.parse_news_titles(html)
            print(f"Знайдено {len(titles)} новин:")
            for i, title in enumerate(titles, 1):
                print(f"{i}. {title}")

# Використання
if __name__ == "__main__":
    parser = PravdaNewsParser()
    parser.run()
