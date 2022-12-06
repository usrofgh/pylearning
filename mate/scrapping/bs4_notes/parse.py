from dataclasses import dataclass
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

URL_BASE = "https://webscraper.io/"
HOME_URL = urljoin(URL_BASE, "test-sites/e-commerce/allinone")


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    reviews: int


def get_single_product(product_soup: BeautifulSoup) -> Product:
    return Product(
        title=product_soup.select_one(".title")["title"],
        description=product_soup.select_one(".description").text,
        price=float(product_soup.select_one(".price").text[1::]),
        rating=int(product_soup.select_one(".ratings p[data-rating]")["data-rating"]),
        reviews=int(product_soup.select_one(".ratings .pull-right").text.split()[0]),
    )


def get_home_products() -> [Product]:
    page = requests.get(HOME_URL).content
    soup = BeautifulSoup(page, "html.parser")
    
    products = soup.select('.thumbnail')

    return [get_single_product(product)
            for product in products]


def main():
    print(get_home_products())


if __name__ == '__main__':
    main()
