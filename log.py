from typing import Callable


class Log:
    """Log class to handle logging messages with different levels and colors."""
    def __init__(self) -> None:
        self.error_msg = self._colorize("[ERROR] ", "red")
        self.info_msg = self._colorize("[INFO] ", "yellow")
        self.run_msg = self._colorize("[RUN] ", "cyan")
        self.bye_msg = self._colorize("[DONE] ", "green")

    def _colorize(self, text: str, color: str) -> Callable[[str], str]:
        """Create a function to colorize log messages based on the specified color."""
        colors = {
            "red": "\033[91m",
            "yellow": "\033[93m",
            "cyan": "\033[96m",
            "green": "\033[92m",
            "reset": "\033[0m",
        }

        def wrapper(message: str) -> str:
            """Wrap the message with the specified color and reset code."""
            return f"{colors[color]}{text}{message}{colors['reset']}"

        return wrapper

    def checking_api_call(self, code_status):
        """Check the status of the API call and log the result."""
        if code_status == 200:
            print(self.info_msg("API call was successful."))
            return True
        else:
            print(self.error_msg("API call failed"))
            return False

    def checking_user_input(self, max_pages: int = 30) -> tuple[int, float]:
        """Check the user input for page number and star rating, ensuring they are within valid ranges."""
        try:
            while True:
                print("How many pages you want to collect? (maximum limit is 30)")
                page_number = int(input(">>> "))

                print("How many stars got at least?")
                stars = float(input(">>> "))

                if (not 1 <= page_number <= max_pages) or (not 1 <= stars <= 5):
                    print(self.error_msg("Invalid input!"))
                else:
                    return page_number, stars
        except ValueError:
            print(self.error_msg("Invalid input!"))
            return 0, 0