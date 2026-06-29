from requests import get
from typing import Generator
from log import Log


class Scraper:
    def __init__(self) -> None:
        self.max_pages = 30
        self.url = "https://api.digikala.com/discovery/api/v1/search"
        self.log = Log()
    
    def get_data(self, title: str, page_number: int) -> Generator | None:
        for page in range(page_number):
            new_url = self.url + f"?page={page + 1}&q={title}"
            data = get(new_url)
            api_response = self.log.checking_api_call(data.status_code)
            if api_response:
                yield data
            else:
                user_answer = str(input("Would you like to try again?(y, n)"))
                if user_answer.lower() == "y":
                    self.get_data(title, page_number)
                else:
                    print(self.log.error_msg("Program stopped!"))
                    return