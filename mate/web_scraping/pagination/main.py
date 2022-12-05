from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    page = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/").content
    soup = BeautifulSoup(page, "html.parser")
    print(soup.prettify())
