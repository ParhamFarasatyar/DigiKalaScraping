from pathlib import Path
import pandas as pd


class Exporter:
    def __init__(self) -> None:
        self.save_path = Path("./data/data.csv")

    def save_data(self, data) -> None:
        self.save_path.parent.mkdir(parents=True, exist_ok=True)

        if not data:
            pd.DataFrame(columns=["title", "stars", "price", "url"]).to_csv(self.save_path, index=False)
            return

        frame = pd.DataFrame.from_dict(data, orient="index")
        frame.to_csv(self.save_path, index_label="product_id")