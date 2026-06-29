from pyfiglet import figlet_format
from scraper import Scraper
from parser import Parser
from exporter import Exporter
from log import Log
from pyfiglet import figlet_format


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
        search_title = str(input(">>> "))
        print("How many pages you want to collect?")
        try:
            while True:
                page_number = int(input(">>> "))
                if not 1 <= page_number <= self.scraper.max_pages:
                    print(self.log.error_msg("Invalid input!"))
                else:
                    break
            while True:
                print("How many stars product got?")
                stars = float(input(">>> "))
                if not 1 <= stars <= 5:
                    print(self.log.error_msg("Invalid input!"))
                    stars = float(input(">>> "))
                else:
                    break
        except ValueError:
            print(self.log.error_msg("Invalid input!"))
            self.run()
        else:
            # Scraper get data from website
            print(self.log.info_msg("Collecting data..."))
            data = self.scraper.get_data(search_title, page_number)
            if data:
                data_iter = iter(data)
            else:
                return

            # Data that we have gotten, sent to parser to exctract data
            print(self.log.info_msg("Exctracting..."))
            data = self.parser.extract_data(data_iter, stars)

            # Save extracted data
            print(self.log.info_msg("Saving in data folder..."))
            self.exporter.save_data(data)

            print(self.log.bye_msg(
                f"Data for {search_title.title()} successfully collected."))



if __name__ == "__main__":
    main = Main()
    main.run()