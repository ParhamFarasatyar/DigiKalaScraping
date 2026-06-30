class Parser:
    """Parser class to extract relevant product data from the scraped data."""
    def __init__(self) -> None:
        """Initialize the Parser class with an empty data dictionary."""
        self.data_dict: dict[str, dict[str, object]] = {}

    def extract_data(self, data, stars: float) -> dict[str, dict[str, object]]:
        """Extract relevant product data from the scraped data based on the star rating filter."""
        self.data_dict = {}
        number_of_product = 1

        for response in data:
            try:
                products = response.json().get("data", {}).get("products", [])
            except Exception:
                continue

            for product in products:
                title_en = product.get("title_en") or ""
                title_fa = product.get("title_fa") or ""
                product_title = title_en or title_fa or "No title"

                default_variant = product.get("default_variant", {}) or {}
                seller = default_variant.get("seller", {}) or {}
                price_info = default_variant.get("price", {}) or {}
                url_info = product.get("url", {}) or {}

                product_stars = seller.get("stars", 0)
                product_price = price_info.get("selling_price", 0)
                product_url = "https://www.digikala.com" + url_info.get("uri", "")

                try:
                    product_stars = float(product_stars)
                except (TypeError, ValueError):
                    product_stars = 0.0

                if product_stars < stars:
                    continue

                self.data_dict[f"product{number_of_product}"] = {
                    "title": product_title,
                    "stars": product_stars,
                    "price": product_price,
                    "url": product_url,
                }
                number_of_product += 1

        return self.data_dict