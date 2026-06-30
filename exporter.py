from pathlib import Path
import pandas as pd


class Exporter:
    """Exporter class to save the extracted product data to a CSV file."""
    def __init__(self) -> None:
        """Initialize the Exporter class with the path to save the CSV file."""
        self.save_path = Path("./data/data.csv")

    def save_data(self, data) -> None:
        """Save the extracted product data to a CSV file."""
        self.save_path.parent.mkdir(parents=True, exist_ok=True)

        if not data:
            pd.DataFrame(columns=["title", "stars", "price", "url"]).to_csv(self.save_path, index=False)
            return

        frame = pd.DataFrame.from_dict(data, orient="index")
        frame.to_csv(self.save_path, index_label="product_id")