import pandas as pd
from pathlib import Path
from os import mkdir


class Exporter:
    def __init__(self) -> None:
        self.save_path = Path("./data/data.csv")
    
    def save_data(self, data) -> None:
        try:
            data = pd.DataFrame(data)
            pd.DataFrame.to_csv(data, self.save_path)
        except OSError:
            mkdir(Path("./data"))
            data = pd.DataFrame(data)
            pd.DataFrame.to_csv(data, self.save_path)