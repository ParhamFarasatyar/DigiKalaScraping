from colorful import colorful as cf


class Log:
    def __init__(self) -> None:
        self.error_msg = cf.red
        self.info_msg = cf.yellow
        self.run_msg = cf.cyan
        self.bye_msg = cf.green
    
    def checking_api_call(self, code_status):
        if code_status == 200:
            print(self.info_msg("API call was successful."))
            return True
        else:
            print(self.error_msg("API call failed"))
            return False
    
    def checking_user_input(self, max_pages: int = 30) -> tuple[int, float]:
        try:
            while True:
                print("How many pages you want to collect?(maximum limit is 30)")
                page_number = int(input(">>> "))

                print("How many stars got at least?")
                stars = float(input(">>> "))

                if (not 1 <= page_number <= max_pages) or (
                    not 1 <= stars <= 5):
                    print(self.error_msg("Invalid input!"))
                else:
                    return page_number, stars
        except ValueError:
            print(self.error_msg("Invalid input!"))
            return 0, 0