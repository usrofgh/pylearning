# почему по дефолту данные в python хранятся именно как dict, а не как другие типы:
# работа с dict имеет O(1). Поэтому классы хранят данные в dict
# compare with list https://prnt.sc/JYkbbY_YRJsh


def get_capital_by_country(countries_list: list, country_to_find: str):
    for (country_name, capital_name) in countries_list:
        if country_name == country_to_find:
            return capital_name

    return "Unknown"


countries_list = [
    ["england", "London"],
    ["germany", "berlin"],
    ["norway", "oslo"],
    ["ukraine", "kyiv"],
]  # O(n) via for

countries_dict = {
    "england": "London",
    "germany": "berlin",
    "norway": "oslo",
    "ukraine": "kyiv",
}


print(countries_dict["ukraine"])  # kyiv // O(1) - не зависит от к-ва входных данных

from time import perf_counter

s = perf_counter()
[get_capital_by_country(countries_list, "norway") for _ in range(10_000_000)]
print(perf_counter() - s)  # 1.51 sec

s = perf_counter()
[countries_dict["norway"] for _ in range(10_000_000)]
print(perf_counter() - s)  # 0.47 sec