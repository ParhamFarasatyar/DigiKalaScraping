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

        page_number, stars = self.log.checking_user_input()
        if page_number and stars:
            # Scraper get data from website
            print(self.log.info_msg("Collecting data..."))
            data = self.scraper.get_data(search_title, page_number)
            if data:
                data_iter = iter(data)
            else:
                print(self.log.error_msg(
                    f"No matches found for {search_title}!"))
                return

            # Data that we have gotten, sent to parser to exctract data
            print(self.log.info_msg("Exctracting..."))
            data = self.parser.extract_data(data_iter, stars)

            # Save extracted data
            print(self.log.info_msg("Saving in data folder..."))
            self.exporter.save_data(data)

            print(self.log.bye_msg(
                f"Data for {search_title.title()} successfully collected."))
        else:
            page_number, stars = self.log.checking_user_input()



if __name__ == "__main__":
    main = Main()
    main.run()