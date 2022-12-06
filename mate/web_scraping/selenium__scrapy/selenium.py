import csv
import logging
import os.path
import sys
import requests

from bs4 import BeautifulSoup
from dataclasses import dataclass, astuple, fields
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.common.by import By

# selenium - не для парсинга, а для автоматического тестирования. Но можно и парсить
#  bs4, scrapy - с их помощью нет возможности нажимать на кнопки


URL_BASE = "https://webscraper.io/"
LAPTOP_URL = urljoin(URL_BASE, "test-sites/e-commerce/static/computers/laptops")

PRODUCTS_OUTPUT_CSV_PATH = "products.csv"


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    reviews: int
    additional_info: dict


PRODUCTS_FIELDS = [field.name for field in fields(Product)]

logging.basicConfig(
    level=logging.DEBUG,  # debug/info - информирование, есть и warning/error. Debug 0-й уровень, потом по возрастанию
    # requests тоже в debug выводит инфо. Поэтому если указали дебаг, то помимо моего также будет выводиться с request
    format="[%(levelname)8s]: %(message)s",  # levelname - занимает 8 символов
    handlers=[  # то, как будут обрабатываться логи
        logging.FileHandler(os.path.join("parser.log")),  # записывает  все в parser.log
        logging.StreamHandler(sys.stdout),  # также будет транслироваться в консоле
    ],
)


def write_products_to_csv(products: [Product]) -> None:
    with open(PRODUCTS_OUTPUT_CSV_PATH, "w") as file:
        writer = csv.writer(file)
        writer.writerow(PRODUCTS_FIELDS)
        writer.writerows([astuple(product) for product in products])


def get_num_pages(soup) -> int:
    count_pages = int(soup.select_one(".pagination .page-item:nth-last-of-type(2)").text)
    if count_pages is None:
        return 1

    return count_pages


def parse_hdd_block_prices(product_soup: BeautifulSoup) -> dict[str, float]:
    # get detalied url
    # Driver get this page
    # Driver find swatches
    # Driver for each button click (if clickable) -> get price
    detailed_url = urljoin(URL_BASE, product_soup.select_one(".title")["href"])
    driver = webdriver.Chrome()


def parse_single_product(product_soup: BeautifulSoup) -> Product:
    hdd_prices = parse_hdd_block_prices(product_soup)

    return Product(
        title=product_soup.select_one(".title")["title"],
        description=product_soup.select_one(".description").text,
        price=float(product_soup.select_one(".price").text[1::]),
        rating=int(product_soup.select_one(".ratings p[data-rating]")["data-rating"]),
        reviews=int(product_soup.select_one(".ratings .pull-right").text.split()[0]),
        additional_info={"hdd_prices": hdd_prices},
    )


def get_single_page_products(page_soup) -> [Product]:
    products = page_soup.select(".thumbnail")
    return [parse_single_product(product) for product in products]


def get_laptop_products() -> [Product]:
    page = requests.get(LAPTOP_URL).content
    first_page_soup = BeautifulSoup(page, "html.parser")

    num_pages = get_num_pages(first_page_soup)

    all_products = get_single_page_products(first_page_soup)

    for page_number in range(2, num_pages):
        logging.info(f"Start parsing page #{page_number}")
        page = requests.get(LAPTOP_URL, {"page": page_number}).content
        soup = BeautifulSoup(page, "html.parser")

        all_products.extend(get_single_page_products(soup))

    return all_products


def main():
    products = get_laptop_products()
    write_products_to_csv(products)


if __name__ == '__main__':
    main()
