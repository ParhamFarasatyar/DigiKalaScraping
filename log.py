from colorful import colorful as cf


class Log:
    def __init__(self) -> None:
        self.error_msg = cf.red
        self.info_msg = cf.yellow
        self.run_msg = cf.cyan
        self.bye_msg = cf.green