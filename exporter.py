import pandas as pd
from pathlib import Path
from colorful import colorful as cf
from os import mkdir


class Exporter:
    def __init__(self) -> None:
        self.save_path = Path("./data/data.csv")
        print(cf.blue("[INFO] Exporter running."))
    
    def save_data(self, data):
        try:
            data = pd.DataFrame(data)
            pd.DataFrame.to_csv(data, self.save_path)
        except OSError:
            mkdir(Path("./data"))
            data = pd.DataFrame(data)
            pd.DataFrame.to_csv(data, self.save_path)