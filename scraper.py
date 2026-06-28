from requests import get


class Scraper:
    def __init__(self) -> None:
        self.max_pages = 30
        self.url = "https://api.digikala.com/discovery/api/v1/search"
    
    def get_data(self, title: str, page_number: int):
        for page in range(page_number):
            new_url = self.url + f"?page={page + 1}&q={title}"
            data = get(new_url)
            yield data