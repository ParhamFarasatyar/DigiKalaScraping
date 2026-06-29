from pyfiglet import figlet_format
from scraper import Scraper
from parser import Parser
from exporter import Exporter
from log import Log


class Main:
    def __init__(self) -> None:
        self.scraper = Scraper()
        self.parser = Parser()
        self.exporter = Exporter()
        self.log = Log()

    def run(self) -> None:
        welcome = figlet_format("DigiKala Scraping!")
        print(self.log.run_msg(welcome))

        print("What do you looking for?")
        search_title = input(">>> ")
        if not search_title:
            print(self.log.error_msg("Search term cannot be empty."))
            return

        page_number, stars = self.log.checking_user_input()
        if page_number <= 0 or stars <= 0:
            return

        print(self.log.info_msg("Collecting data..."))
        data = self.scraper.get_data(search_title, page_number)
        if not data:
            print(self.log.error_msg(f"No matches found for {search_title}!"))
            return

        print(self.log.info_msg("Extracting..."))
        parsed_data = self.parser.extract_data(data, stars)
        if not parsed_data:
            print(self.log.error_msg(f"No products matched your rating filter for {search_title}."))
            return

        print(self.log.info_msg("Saving in data folder..."))
        self.exporter.save_data(parsed_data)

        print(self.log.bye_msg(f"Data for {search_title.title()} successfully collected."))


if __name__ == "__main__":
    main = Main()
    main.run()