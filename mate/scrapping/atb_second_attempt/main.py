import itertools
import random

import httpx
import csv
import os

import asyncio
from bs4 import BeautifulSoup
from proxy_auth import proxies
from proxy_auth import user_agent_list

request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9,ru;q=0.8,uk;q=0.7",
    "cache-control": "max-age=0"
}

URL_HOME = "https://www.atbmarket.com/"


def get_data():
    is_exist = os.path.exists("data")
    if is_exist is False:
        os.mkdir("data")

    # r = requests.get(URL_HOME, headers=request_header)
    # with open("data/index.html", "w", encoding="UTF-8") as file:
    #     file.write(r.text)

    # with open("data/index.html", encoding="UTF-8") as file:
    #     page = file.read()
    #
    # page_soup = BeautifulSoup(page, "html.parser")
    # links_of_last_page_categories = [urljoin(URL_HOME, link["href"])
    #                                  for link in page_soup.select(".category-menu__link-wrap")[3::]]
    #
    # all_category_links = []
    # for link in links_of_last_page_categories:
    #     response = requests.get(urljoin(link, "?page=500"), headers=request_header).content
    #     page_soup = BeautifulSoup(response, "html.parser")
    #     try:
    #         n_pages = int(page_soup.select_one(".active .product-pagination__link").text)
    #     except AttributeError:
    #         n_pages = 1
    #
    #     all_category_links.extend([urljoin(link, f"?page={i}") for i in range(1, n_pages + 1)])
    #
    # with open("data/all_category_links.txt", "w") as file:
    #     for link in all_category_links:
    #         file.write(f"{link}\n")

    # with open("data/all_category_links.txt", "r") as file:
    #     all_category_links = file.readlines()
    #
    # links_to_product_page = []
    # count = len(all_category_links)
    # print(f"Всего ссылок: {count}")
    #
    # for category_link in all_category_links:
    #     print(f"Осталось: {count}")
    #     count -= 1
    #
    #     r = requests.get(category_link, headers=request_header).content
    #     page_soup = BeautifulSoup(r, "html.parser")
    #     link_to_product = [urljoin(URL_HOME, link["href"])
    #                        for link in page_soup.select(".catalog-page__list .catalog-item__title a")]
    #     links_to_product_page.extend(link_to_product)
    #
    # with open("data/products_links.txt", "w", encoding="UTF-8") as file:
    #     for link in links_to_product_page:
    #         file.write(f"{link}\n")

with open("data/products_links.txt", "r", encoding="UTF-8") as file:
    links_to_product_page = file.readlines()

products = []


async def async_requests(product_link: str, client: httpx.AsyncClient):

    response = await client.get(product_link, headers=request_header)
    page_soup = BeautifulSoup(response.content, "html.parser")
    print(f"response from {product_link.strip()}")

    try:
        category = page_soup.select_one(".breadcrumbs__item:nth-last-child(2) a")["href"].split("/")[-1].partition("-")[-1]
        title = page_soup.select_one(".page-title.product-page__title").text
        code = page_soup.select_one(".custom-tag__text strong").text
        rating = page_soup.select_one(".product-main .rating__value").text
        in_stock = None
    except:
        print(f"{response.status_code} -----", response.url)
        file_error = str(response.url).rsplit("/")[-1]
        with open(f"errors/{file_error}.html", "w", encoding="UTF-8") as file:
            file.write(response.text)

    if page_soup.select_one(".product-main .available-tag--grey"):
        in_stock = "no"
    elif page_soup.select_one(".product-main .available-tag--orange"):
        in_stock = "ends"
    elif page_soup.select_one(".product-main .product-about__available"):
        in_stock = "yes"

    try:
        original_price = page_soup.select_one(".product-main .product-price__bottom").text.strip().split()[0]
        discount_price = page_soup.select_one(".product-main .product-price__top").text.strip().split()[0]
    except AttributeError:
        original_price = page_soup.select_one(".product-main .product-price__top").text.strip().split()[0]
        discount_price = None

    names = [name.text.strip() for name in
             page_soup.select(".product-characteristics__row .product-characteristics__name")]
    values = [value.text.strip() for value in
              page_soup.select(".product-characteristics__row .product-characteristics__value")]
    characteristics = dict(zip(names, values))

    try:
        description = page_soup.select_one(".product-characteristics__desc p").text
    except AttributeError:
        description = None

    comments_list = page_soup.select(".reviews-item__main")
    comments = []
    if len(comments_list) == 0:
        comments = None
    else:
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

    return {
        "title": title,
        "code": code,
        "in_stock": in_stock,
        "category": category,
        "rating": rating,
        "original_price": original_price,
        "discount_price": discount_price,
        "characteristics": characteristics,
        "description": description,
        "comments": comments,
    }


async def aparse_products():
    clients = []
    for proxy in proxies:
        clients.append(httpx.AsyncClient(proxies=proxy))

    proxy_iterator_cycle = itertools.cycle(iter(clients))

    return await asyncio.gather(*[async_requests(link, next(proxy_iterator_cycle))
                                  for link in links_to_product_page])
    # async with httpx.AsyncClient(proxies=proxies[n_proxy]) as client:
    #     return await asyncio.gather(
    #         *[async_requests(link, client)]
    #     )


# def parse_products():
#     return [async_requests(link) for link in links_to_product_page]


def main():
    get_data()

if __name__ == '__main__':
    products = asyncio.run(aparse_products())
    # products = parse_products()
    with open("data/products.csv", "w", encoding="UTF-8", newline="") as file:
        writer = csv.writer(file)
        csv_titles = products[0].keys()
        writer.writerow(csv_titles)
        for product in products:
            writer.writerow(product.values())