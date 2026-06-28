from pyfiglet import figlet_format
from colorful import colorful as cf
from scraper import Scraper
from parser import Parser
from exporter import Exporter


class Main:
    def __init__(self) -> None:
        self.invalid_input = cf.red("invalid input!")
        self.scraper = Scraper()
        self.parser = Parser()
        self.exporter = Exporter()

    def run(self):
        print("What do you looking for?")
        search_title = str(input(">>> "))
        print("How many pages you want to collect?")
        try:
            page_number = int(input(">>> "))
            print("How many stars product got?")
            while True:
                stars = float(input(">>> "))
                if not 1 <= stars <= 5:
                    print(self.invalid_input)
                    stars = float(input(">>> "))
                else:
                    break
        except ValueError:
            print(self.invalid_input)
        else:
            # Scraper get data from website
            data_iter = iter(self.scraper.get_data(search_title, page_number))

            # Data that we have gotten, sent to parser to exctract data
            data = self.parser.extract_data(data_iter, stars)

            # Save extracted data
            self.exporter.save_data(data)



if __name__ == "__main__":
    main = Main()
    main.run()