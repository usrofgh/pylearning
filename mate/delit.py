import asyncio
import multiprocessing
import threading
import httpx
import time

URL = "https://www.google.com/"


def send_request(i, url: str) -> None:
    response = httpx.get(url)
    print(i, response.status_code)


def main_threading() -> None:
    tasks = []
    for i in range(100):
        tasks.append(threading.Thread(target=send_request, args=(i, URL)))
        tasks[-1].start()

    for task in tasks:
        task.join()


def main_processing() -> None:
    tasks = []
    for i in range(100):
        tasks.append(multiprocessing.Process(target=send_request, args=(i, URL)))
        tasks[-1].start()

    for task in tasks:
        task.join()


async def asend_request(i, URL, client: httpx.AsyncClient) -> None:
    response = await client.get(URL)
    print(i, response.status_code)


async def main_asyncio():
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(
            *[asend_request(i, URL, client) for i in range(100)]
        )
if __name__ == '__main__':
    s = time.perf_counter()
    # main_threading()
    # main_processing()
    asyncio.run(main_asyncio())

    e = time.perf_counter()
    print(e - s, ' sec.')
