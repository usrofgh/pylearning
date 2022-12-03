from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, wait
import multiprocessing
import httpx
import time

URL = "https://www.google.com/"
n = 100


def send_request(i: int, url: str) -> None:
    response = httpx.get(url)
    print(i, response.status_code)


def main_thread() -> None:
    futures = []

    with ThreadPoolExecutor() as executor:
        for i in range(n):
            futures.append(executor.submit(send_request, i, URL))
    wait(futures)


def main_multiprocess() -> None:
    tasks = []

    for i in range(n + 1):
        tasks.append(multiprocessing.Process(target=send_request, args=(i, URL)))
        tasks[-1].start()

    for task in tasks:
        task.join()


async def async_send_request(i: int, url: str, client: httpx.AsyncClient) -> None:
    response = await client.get(url)
    print(i, response.status_code)



if __name__ == '__main__':
    start = time.perf_counter()
    # main_thread()  # 2.2 sec
    end = time.perf_counter()
    print('Elapsed: ', end - start)