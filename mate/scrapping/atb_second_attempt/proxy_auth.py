import random

usa_login = "tzWQf4"
usa_password = "rCswtn"

gen_login6 = "3TZ72P"
gen_password6 = "Z5NSnE"

user_agent_list = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',

]

proxies = [
    {"https://": f"http://{usa_login}:{usa_password}@131.108.17.115:9579"},
    {"https://": f"http://{usa_login}:{usa_password}@131.108.17.20:9713"},
    {"https://": f"http://{usa_login}:{usa_password}@138.59.207.11:9218"},
]
