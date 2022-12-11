import csv
import logging
import os
import sys

from dataclasses import dataclass, fields, astuple
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


@dataclass
class Product:
    title: str
    description: str
    price: float
    count_reviews: int
    rating: int
    additional_info: [dict]


_driver: WebDriver | None = None
HEADERS = [field.name for field in fields(Product)]
URL_BASE = "https://webscraper.io/"

URLS_FOR_PARSING = {
    "home": "https://webscraper.io/test-sites/e-commerce/more",
    "laptop": "https://webscraper.io/test-sites/e-commerce/more/computers/laptops",
    "computer": "https://webscraper.io/test-sites/e-commerce/more/computers",
    "tablet": "https://webscraper.io/test-sites/e-commerce/more/computers/tablets",
    "phone": "https://webscraper.io/test-sites/e-commerce/more/phones",
    "touch": "https://webscraper.io/test-sites/e-commerce/more/phones/touch",
}


def get_driver() -> WebDriver:
    return _driver


def set_driver(new_driver: WebDriver) -> None:
    global _driver
    _driver = new_driver


logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)8s]: %(message)s",
    handlers=[
        logging.FileHandler(os.path.join("../parser.log")),
        logging.StreamHandler(sys.stdout),
    ],
)


def write_to_csv(path_to_csv: str, products: [Product]) -> None:
    with open(path_to_csv, "w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(HEADERS)
        writer.writerows([astuple(product) for product in products])


def accept_cookies() -> None:
    get_driver().find_element(By.CLASS_NAME, "acceptCookies").click()


def get_urls_categories() -> [str]:
    url = "https://webscraper.io/test-sites/e-commerce/more"
    driver = webdriver.Chrome()
    driver.get(url)


def get_swatches() -> {str: str}:
    driver = get_driver()

    swatches = driver.find_elements(By.CLASS_NAME, "swatches")
    if len(swatches) == 0:
        return {}

    buttons = swatches[0].find_elements(By.TAG_NAME, "button")

    prices = {}
    for btn in buttons:
        if not btn.get_property("disabled"):
            btn.click()
            prices[btn.get_property("value")] = float(driver.find_element(
                By.CLASS_NAME, "price"
            ).text.replace("$", ""))

    return {"swatches": prices} if prices else {}


def get_colors(card) -> {str: str}:
    colors = [color.text
              for color in
              card.find_elements(By.CSS_SELECTOR, ".dropdown option[value]")[1::]]

    return {"colors": colors} if colors else {}


def get_additional_info(card) -> dict:
    colors = get_colors(card)
    swatches = get_swatches()
    additional_info = colors | swatches
    return additional_info


def get_product_info_by_link(full_link: str) -> Product:
    driver = get_driver()
    driver.get(full_link)
    card = driver.find_element(By.CLASS_NAME, "thumbnail")

    title = card.find_elements(By.CSS_SELECTOR, ".caption h4")[-1].text
    price = float(card.find_element(By.CSS_SELECTOR, ".caption .price").text.replace("$", ""))
    description = card.find_element(By.CSS_SELECTOR, ".description").text
    count_reviews = int(card.find_element(By.CSS_SELECTOR, ".ratings p").text.split()[0])
    rating = len(card.find_elements(By.CSS_SELECTOR, ".ratings .glyphicon-star"))
    additional_info = get_additional_info(card)

    return Product(
        title=title,
        price=price,
        description=description,
        count_reviews=count_reviews,
        rating=rating,
        additional_info=additional_info,
    )


def over_more_pagination(more_btn: list) -> None:
    if len(more_btn) == 0:
        return
    more_btn = more_btn[0]

    while True:
        if more_btn.is_displayed():
            more_btn.click()
            sleep(0.2)
        else:
            break


def get_links_of_detailed_product_info(full_url: str) -> [str]:
    driver = get_driver()
    driver.get(full_url)

    accept_cookies()
    more_btn = driver.find_elements(By.CLASS_NAME, "ecomerce-items-scroll-more")
    over_more_pagination(more_btn)

    links_to_products = [link.get_attribute("href")
                         for link in driver.find_elements(By.CSS_SELECTOR, ".thumbnail .title")]
    return links_to_products


def get_all_products() -> None:
    with webdriver.Chrome() as new_driver:
        set_driver(new_driver)
        for category_name, url in URLS_FOR_PARSING.items():
            links = get_links_of_detailed_product_info(url)
            products = [*map(get_product_info_by_link, links)]
            write_to_csv(f"{category_name}.csv", products)


if __name__ == '__main__':
    get_all_products()
