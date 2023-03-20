import json
import time
import threading
import asyncio
from urllib.request import Request, urlopen

import aiofiles as aiofiles
import aiohttp as aiohttp

URL = "https://binaryjazz.us/wp-json/genrenator/v1/genre/"
user_agent = {"User-Agent": "Mozilla/5.0"}
n = 100


def write_genre(file_name):

    req = Request(URL, headers={**user_agent})
    genre = json.load(urlopen(req))

    with open(file_name, "w") as new_file:
        print(f"Writing '{genre}' to '{file_name}'...")
        new_file.write(genre)


async def async_write_genre(file_name):

    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            genre = await response.json()

    async with aiofiles.open(file_name, "w") as new_file:
        print(f"Writing '{genre}' to '{file_name}'...")
        await new_file.write(genre)


if __name__ == "__main__":

    threads = []
    print("Starting...")
    start = time.time()

    for i in range(n):
        write_genre(f"./test/test_file{i}.txt")

    # for i in range(n):
    #     thread = threading.Thread(
    #         target=write_genre,
    #         args=[f"./test/test_file{i}.txt"]
    #     )
    #     thread.start()
    #     threads.append(thread)
    #
    # for thread in threads:
    #     thread.join()

    

    end = time.time()
    try:
        print(f"Time to complete threading read/writes: {round(end - start, 2)} seconds")  # 12.31 sec. | 31.36 sec.
    except UnicodeError:
        pass