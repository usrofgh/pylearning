import csv
import requests
import logging
import os.path
import sys


from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from dataclasses import dataclass, astuple, fields
from urllib.parse import urljoin

from selenium.webdriver.remote.webdriver import WebDriver

URL_BASE = "https://webscraper.io/"
LAPTOP_URL = urljoin(URL_BASE, "test-sites/e-commerce/allinone/computers/laptops")

PRODUCTS_OUTPUT_CSV_PATH = "products.csv"


@dataclass
class Product:
    title: str
    description: str
    price: float
    rating: int
    reviews: int
    additional_info: dict


_driver: WebDriver | None = None
PRODUCTS_FIELDS = [field.name for field in fields(Product)]


def get_driver() -> WebDriver:
    return _driver


def set_driver(new_driver: WebDriver) -> None:
    global _driver
    _driver = new_driver



logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)8s]: %(message)s",
    handlers=[
        logging.FileHandler(os.path.join("parser.log")),
        logging.StreamHandler(sys.stdout),
    ],
)


def write_products_to_csv(products: [Product]) -> None:
    with open(PRODUCTS_OUTPUT_CSV_PATH, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(PRODUCTS_FIELDS)
        writer.writerows([astuple(product) for product in products])


def get_num_pages(soup) -> int:
    count_pages = soup.select_one(".pagination .page-item:nth-last-of-type(2)")
    if count_pages is None:
        return 1
    return int(count_pages.text)


def parse_hdd_block_prices(product_soup: BeautifulSoup) -> dict[str, float]:
    detailed_url = urljoin(URL_BASE, product_soup.select_one(".title")["href"])
    driver = get_driver()
    driver.get(detailed_url)
    swatches = driver.find_element(By.CLASS_NAME, "swatches")
    buttons = swatches.find_elements(By.TAG_NAME, "button")

    prices = {}
    for btn in buttons:
        if not btn.get_property("disabled"):
            btn.click()
            prices[btn.get_property("value")] = float(driver.find_element(
                By.CLASS_NAME, "price"
            ).text.replace("$", ""))

    return prices




def parse_single_product(product_soup: BeautifulSoup) -> Product:
    hdd_prices = parse_hdd_block_prices(product_soup)

    return Product(
        title=product_soup.select_one(".title")["title"],
        description=product_soup.select_one(".description").text,
        price=float(product_soup.select_one(".price").text[1::]),
        rating=int(product_soup.select_one(".ratings p[data-rating]")["data-rating"]),
        reviews=int(product_soup.select_one(".ratings .pull-right").text.split()[0]),
        additional_info=hdd_prices,
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
        break  # TODO: remove this - just for debugging

    return all_products


def main():
    with webdriver.Chrome() as new_driver:
        set_driver(new_driver)
        products = get_laptop_products()
        write_products_to_csv(products)


if __name__ == '__main__':
    main()
