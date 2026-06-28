from colorful import colorful as cf


class Parser:
    def __init__(self) -> None:
        print(cf.blue("[Info] Parser running."))
    
    def extract_data(self, data):
        for i in data:
            print(i.status_code)