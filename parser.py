class Parser:
    def __init__(self) -> None:
        self.data_dict = {}
    
    def extract_data(self, data, stars):
        for products in data:
            for i, product in enumerate(products.json()["data"]["products"]):
                product_title = product["title_en"]
                if not product_title:
                    product_title = product["title_fa"]

                product_stars = product["default_variant"]["seller"]["stars"]
                product_price = product["default_variant"]["price"]["selling_price"]
                product_url = "https://www.digikala.com" + product["url"]["uri"]

                if product_stars < stars:
                    continue

                self.data_dict[f"product{i + 1}"] = {
                    "title": product_title,
                    "stars": product_stars,
                    "price": product_price,
                    "url": product_url
                    }
        
        return self.data_dict