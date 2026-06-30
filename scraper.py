import requests
from log import Log


class Scraper:
    """Scraper class to handle API requests and data collection."""
    def __init__(self) -> None:
        """Initialize the Scraper class with the maximum number of pages and the API URL."""
        self.max_pages = 30
        self.url = "https://api.digikala.com/discovery/api/v1/search"
        self.log = Log()

    def get_data(self, title: str, page_number: int) -> list:
        """Get the data from the API based on the search title and page number."""
        responses = []
        for page in range(1, page_number + 1):
            response = None
            for attempt in range(3):
                try:
                    response = requests.get(
                        self.url,
                        params={"page": page, "q": title},
                        timeout=10,
                    )
                    break
                except requests.RequestException as exc:
                    if attempt == 2:
                        print(self.log.error_msg(f"Request failed: {exc}"))
                        return responses
                    continue

            if response is None:
                return responses

            api_response = self.log.checking_api_call(response.status_code)
            if api_response:
                responses.append(response)
            else:
                print(self.log.error_msg(f"Program stopped while fetching page {page}!"))
                break

        return responses