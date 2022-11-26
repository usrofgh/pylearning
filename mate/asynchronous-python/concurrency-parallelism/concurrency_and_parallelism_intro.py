import asyncio
import multiprocessing
import threading
import time
import httpx  # похожий на requests, только поддерживает асинхронность

URL = "https://www.google.com/"

n = 50


def send_request(num: int, url: str):
    print(f"Sending request #{num}")
    response = httpx.get(url)
    print(response.status_code)


def main_sync():
    for i in range(n):
        send_request(i, URL)  # Выполняем след. Запрос после окончания предыдущего. Заняло 6 сек


#----------------------------------------------------------------------------------------------------------------------
# Есть 3 подхода для ускорения скрипта
# 1-й подход - работа с потоками


def main_threads():
    tasks = []

    for i in range(n):
        tasks.append(threading.Thread(target=send_request, args=(i, URL)))
        tasks[-1].start()

    for task in tasks:
        task.join()
#----------------------------------------------------------------------------------------------------------------------
# 2-й подход - работа с процессами


def main_processes():  # Так же как и выше, только с помощью процессов, а не потоков
    tasks = []

    for i in range(n):
        tasks.append(multiprocessing.Process(target=send_request, args=(i, URL)))
        tasks[-1].start()

    for task in tasks:
        task.join()
#----------------------------------------------------------------------------------------------------------------------
# 3-й подход - asyncio. Появился с python 3.5. Стал стандартным с 3.7


async def async_send_request(num: int, url: str, client: httpx.AsyncClient):
    print(f"Sending request #{num}")
    response = await client.get(url)
    print(response.status_code)


async def main_asyncio():
    async with httpx.AsyncClient() as client:
        return await asyncio.gather(
            *[async_send_request(num, URL, client) for num in range(n)]
        )



if __name__ == "__main__":
    start = time.perf_counter()
    # 50 запросов:
    # main_sync()  # 28.25 сек
    # main_threads()  # 0.72 сек
    # main_processes()  # 2.16 сек
    asyncio.run(main_asyncio())  # 0.65 сек
    end = time.perf_counter()

    print("Elapsed", end - start)