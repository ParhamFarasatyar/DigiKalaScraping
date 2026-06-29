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