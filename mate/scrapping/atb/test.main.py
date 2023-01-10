import asyncio
import csv
import json
import logging
import os
import sys
import time
from dataclasses import dataclass, fields, astuple
from urllib.parse import urljoin

import httpx as httpx
from bs4 import BeautifulSoup
import requests
from httpx import AsyncClient

headers = {  # TODO: add user-agent lib changer
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/108.0.0.0 Safari/537.36"
}



@dataclass
class ATBProduct:
    _code: int
    _in_stock: str
    _category: str
    _title: str
    _original_price: float
    _discount_price: float
    _discount_amount: str
    _discount_date: str
    _rating: str
    _description: str
    _characteristics: dict
    _comments: list
    
    def __init__(self, page):
        self._set_code(page)
        self._set_in_stock(page)
        self._set_category(page)
        self._set_title(page)
        self._set_price(page)
        self._set_discount_amount(page)
        self._set_discount_date(page)
        self._set_rating(page)
        self._set_description(page)
        self._set_characteristic(page)
        self._set_comments(page)

    def __str__(self):
        print("category:", self.get_category())
        print("title:", self.get_title())
        print("code:", self.get_code())
        print("original price:", self.get_original_price())
        print("discount price:", self.get_discount_price())
        print("discount_info:", self.get_discount_date())
        print("discount_info:", self.get_discount_amount())
        print("stock status:", self.get_stock_status())
        print("rating:", self.get_rating())
        print("description:", self.get_description())
        print("comments:", self.get_comments())
        return ""

    def _set_category(self, page):
        try:
            self._category = page.select_one(".breadcrumbs__item:nth-last-child(2) a")["href"].split("/")[-1].partition("-")[-1]
        except AttributeError:
            print("error", page.select_one("link[hreflang]")["href"])
            self._category = None
        except:
            print("error", page.select_one("link[hreflang]")["href"])

    def _set_characteristic(self, page):
        names = [name.text.strip() for name in page.select(".product-characteristics__row .product-characteristics__name")]
        values = [value.text.strip() for value in page.select(".product-characteristics__row .product-characteristics__value")]
        self._characteristics = dict(zip(names, values))
        

    def _set_title(self, page: BeautifulSoup):
        try:
            self._title = page.select_one(".page-title.product-page__title").text
        except AttributeError:
            print(page.select_one("link[hreflang]")["href"])
            self._title = None
        except:
            print(page.select_one("link[hreflang]")["href"])

    def _set_code(self, page):
        try:
            self._code = page.select_one(".custom-tag__text strong").text
        except AttributeError:
            self._code = None
        except:
            print(page.select_one("link[hreflang]")["href"])

    def _set_price(self, page):
        try:
            prices = page.select_one(".product-main .product-price--sale").text
            self._original_price = prices.select_one(".product-price__bottom").text.strip().split()[0]
            self._discount_price = prices.select_one(".product-price__top").text.strip().split()[0]
        except AttributeError:
            self._original_price = page.select_one(".product-main .product-price__top").text.strip().split()[0]
            self._discount_price = None
        except:
            print(page.select_one("link[hreflang]")["href"])



    def _set_discount_amount(self, page):
        try:
            temp = page.select_one(".product-about__labels .custom-product-label").text
        except AttributeError:
            self._discount_amount = None
            return
        except:
            print(page.select_one("link[hreflang]")["href"])
        if "-" in temp:
            self._discount_amount = temp[1::]
        else:
            self._discount_amount = None


    def _set_discount_date(self, page):
        try:
            interval_discount = page.select_one(".product-about__dates span:nth-child(2)").text
        except AttributeError:
            self._discount_date = None
            return
        except:
            print(page.select_one("link[hreflang]")["href"])

        interval_discount = interval_discount.split(" – ")
        start = interval_discount[0]
        stop = interval_discount[1]
        self._discount_date = {"start": start, "end": stop}

    def _set_in_stock(self, page):
        if page.select_one(".product-main .available-tag--grey"):
            self._in_stock = "no"
        elif page.select_one(".product-main .available-tag--orange"):
            self._in_stock = "ends"
        elif page.select_one(".product-main .product-about__available"):
            self._in_stock = "yes"

    def _set_rating(self, page):
        self._rating = page.select_one(".product-main .rating__value").text

    def _set_description(self, page):
        try:
            self._description = page.select_one(".product-characteristics__desc p").text
        except AttributeError:
            self._description = None
        except:
            print(page.select_one("link[hreflang]")["href"])

    def _set_comments(self, page):
        comments_list = page.select(".reviews-item__main")
        comments = []
        if len(comments_list) == 0:
            self._comments = None
            return

        for comment in comments_list:
            name = comment.select_one(".reviews-item__info .reviews-item__name").text
            date = comment.select_one(".reviews-item__time").text
            date_temp = date.split(".")
            date = f"{date_temp[0]}.{date_temp[1]}.{date_temp[-1]}"
            try:
                rating = comment.select_one(".rating input:checked")["id"].split("-")[-1]
            except TypeError:
                rating = None
            text_comment = comment.select_one(".reviews-item__desc").text


            comments.append({"date": date,
                             "name": name,
                             "rating": rating,
                             "text": text_comment.strip()})
        self._comments = comments

    def get_category(self):
        return self._category

    def get_title(self):
        return self._title

    def get_code(self):
        return self._code

    def get_original_price(self):
        return self._original_price

    def get_discount_price(self):
        return self._discount_price

    def get_discount_date(self):
        return self._discount_date

    def get_discount_amount(self):
        return self._discount_amount

    def get_stock_status(self):
        return self._in_stock

    def get_rating(self):
        return self._rating

    def get_description(self):
        return self._description

    def get_comments(self):
        return self._comments


HOME_PAGE = "https://www.atbmarket.com/"
# with open("data/index.html", "r", encoding="UTF-8") as file:
#     page = file.read()
#     print("index.html is read")
home_page_soup = BeautifulSoup(page, "html.parser")
categories_base_links = [urljoin(HOME_PAGE, i["href"])
                    for i in home_page_soup.select(".category-menu a.category-menu__link-wrap")[3::]]
#
# for category_link in categories_base_links:
#     category_page = requests.get(category_link,
#                                  params={"page": 500}, headers=headers).content
#     category_page_soup = BeautifulSoup(category_page, "html.parser")
#     try:
#         count_page = category_page_soup.select_one(".product-pagination__list .active").text
#     except AttributeError:
#         count_page = 1
#
#     category_links = []
#     for n_page in range(1, int(count_page) + 1):
#         category_links.append(urljoin(category_link, f"?page={n_page}"))
#
#     for lnk in category_links:
#         print(logging.INFO)
#         with open("data/categories_links.txt", "a", encoding="UTF-8") as file:
#             file.write(lnk)
#             file.write("\n")



# with open("data/categories_links.txt", "r", encoding="UTF-8") as file:
#     generated_category_links = file.read().split("\n")[:-1]
# category_links = []
# for category_link in generated_category_links:
#     page = requests.get(category_link, headers=headers).content  # TODO: do it with scrapy/asyncio
#     print(f"request to {category_link}")
#     page_soup = BeautifulSoup(page, "html.parser")
#     category_links.extend([
#         urljoin(HOME_PAGE, item["href"])
#         for item in page_soup.select(".catalog-list .catalog-item__title a")
#     ])
#
# with open("data/all_products_links.txt", "a", encoding="UTF-8") as file:
#     for link in category_links:
#         file.write(link)
#         file.write("\n")




with open("data/all_products_links.txt", "r", encoding="UTF-8") as file:
    all_roduct_links = file.read().split("\n")[:-1]


async def async_requests(link_page, client: httpx.AsyncClient):
    response = await client.get(link_page, headers=headers)
    print(f"got response from {link_page}")
    return ATBProduct(BeautifulSoup(response.content, "html.parser"))


async def async_parse():
    print(all_roduct_links[-1])
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(*[async_requests(link_page, client)
                                   for link_page in all_roduct_links])



if __name__ == '__main__':
    start_time = time.perf_counter()
    all_roducts = asyncio.run(async_parse())
    end_time = time.perf_counter()
    print("Elapsed:", end_time - start_time)
    print("processed count of products:", len(all_roducts))
    count = 0

    with open("product_test.csv", "w", encoding="UTF-8", newline="") as file:
        csv_headers = [field.name for field in fields(ATBProduct)]
        writer = csv.writer(file)
        writer.writerow(csv_headers)
        for product in all_roducts:
            writer.writerow(astuple(product))
            count += 1
            print(f"{count} written")

