from dataclasses import astuple, dataclass
from urllib.parse import urljoin

import bs4
from bs4 import BeautifulSoup
import requests


HOME_PAGE = "https://www.atbmarket.com/"
headers = {  # TODO: add user-agent lib changer
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36"
}

class ATBProduct:
    def __init__(self, page):
        self._set_title(page)
        self._set_code(page)
        self._set_original_price(page)
        self._set_discount_price(page)
        self._set_discount_info(page)
        self._set_in_stock(page)
        self._set_rating(page)
        self._set_brand(page)
        self._set_country(page)
        self._set_description(page)
        self._set_comments(page)

    def _set_title(self, page):
        self._title = page.select_one(".page-title.product-page__title").text

    def _set_code(self, page):
        self._code = page.select_one(".custom-tag__text strong").text

    def _set_original_price(self, page):
        self._original_price = page.select_one(".product-main .product-price__top").text.strip().split()[0]

    def _set_discount_price(self, page):
        try:
            self._discount_price = page.select_one(".product-main .product-price__bottom").text
        except:
            self._discount_price = None

    def _set_discount_info(self, page):
        interval_discount = page.select_one(".product-about__dates span:nth-child(2)")
        if interval_discount is None:
            self._discount_info = None
            return
        start = interval_discount.split("-")[0].strip()
        stop = interval_discount.split("-")[1].strip()
        self._discount_info = {"date": {"start": start, "end": stop}}

    def _set_in_stock(self, page):
        self._in_stock = bool(page.select_one(".available-tag.available-tag--grey"))

    def _set_rating(self, page):
        self._rating = page.select_one(".product-main .rating__value").text

    def _set_brand(self, page):
        self._brand = page.select("#productCharacteristics "
                                  ".product-characteristics__value")[1].text

    def _set_country(self, page):
        self._country = page.select("#productCharacteristics .product-characteristics__value")[0].text

    def _set_description(self, page):
        desc = page.select_one(".product-characteristics__desc p")
        if desc is not None:
            self._desc = desc.text
        else:
            self._desc = None

    def _set_comments(self, page):
        comments_list = page.select(".reviews-item__main")
        comments = []
        if len(comments) == 0:
            self._comments = None
            return
        for comment in comments_list:
            name = comment.select_one(".reviews-item__info .reviews-item__name")
            date = comment.select_one(".reviews-item__time")
            rating = comment.select_one(".rating")

            comments.append({"name": name,
                             "date": date,
                             "rating": rating})
            self._comments = comment

    def get_title(self):
        return self._title

    def get_code(self):
        return self._code

    def get_original_price(self):
        return self._original_price

    def get_discount_price(self):
        return self._discount_price

    def get_discount_info(self):
        return self._discount_info

    def get_stock_status(self):
        return self._in_stock

    def get_rating(self):
        return self._rating

    def get_brand(self):
        return self._brand

    def get_country(self):
        return self._country

    def get_description(self):
        return self._desc

    def get_comments(self):
        return self._comments


def reading(path: str):
    with open(path, "r", encoding="UTF-8") as file:
        return file.read()


def writing(path: str, type_writing: str, item):
    with open(path, type_writing, encoding="UTF-8") as file:
        file.write(item)

# TODO: ...
# home_page = requests.get(HOME_PAGE, headers).text
# writing(item=home_page, add_write="w", path="data/index.html")

# categories_pages = []
#
# page = reading("data/index.html")
# home_page_soup = bs4.BeautifulSoup(page, "html.parser")
# categories_links = [urljoin(HOME_PAGE, i["href"])
#                     for i in home_page_soup.select(".category-menu a.category-menu__link-wrap")[3::]]

# for category_link in categories_links[1:2]:  # TODO: delete [0:1]
    # TODO:
    # category_page = requests.get(category_link,
    #                              params={"page": 500}, headers=headers).text
    # writing(category_page, "a", "data/category_page.html")


    # category_page = reading("data/category_page.html")
    # category_page_soup = bs4.BeautifulSoup(category_page, "html.parser")
    # count_page = category_page_soup.select_one(".product-pagination__list .active").text
    #
    # if count_page is None:
    #     count_page = 1
    # TODO: GENERATING PAGES
    # for n_page in range(1, int(count_page) + 1):
    #     categories_pages.append(urljoin(category_link, f"?page={n_page}"))
    # TODO: WRITING GENERATED PAGES
    # with open("data/categories_pages.txt", "a", encoding="UTF-8") as f:
    #     my_iter = iter(categories_pages)
    #     f.write(next(my_iter, ''))
    #     for line in my_iter:
    #         f.write('\n')
    #         f.write(line)

# generated_category_pages = reading("data/categories_pages.txt")
# page = generated_category_pages.split("\n")[0]
# page_soup = BeautifulSoup(page, "html.parser")

# category_page_soup = bs4.BeautifulSoup(reading("data/category_page.html"), "html.parser")
# links = [urljoin(HOME_PAGE, item["href"])
#          for item in category_page_soup.select(".catalog-list .catalog-item__title a")]
# product = requests.get(links[0], headers=headers).text
# writing(item=product, type_writing="w", path="data/product.html")

page = BeautifulSoup(reading("data/product.html"), "html.parser")
atb_product = ATBProduct(page)
print(atb_product.get_title())
print(atb_product.get_code())
print(atb_product.get_original_price())
print(atb_product.get_discount_price())
print(atb_product.get_discount_info())
print(atb_product.get_stock_status())
print(atb_product.get_rating())
print(atb_product.get_brand())
print(atb_product.get_country())
print(atb_product.get_description())
print(atb_product.get_comments())
