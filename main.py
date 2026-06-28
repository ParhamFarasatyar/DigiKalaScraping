from pyfiglet import figlet_format
from colorful import colorful as cf
from scraper import Scraper
from parser import Parser


class Main:
    def __init__(self) -> None:
        self.invalid_input = cf.red("invalid input!")
        self.scraper = Scraper()
        self.parser = Parser()

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
            data_iter = iter(self.scraper.get_data(search_title, page_number))
            print("hello")


if __name__ == "__main__":
    main = Main()
    main.run()