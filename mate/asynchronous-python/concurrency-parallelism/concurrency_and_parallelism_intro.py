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
# 1-й подход - работа с потоками(конкурентность).
# Поскольку есть io blocking operations - выигрыш в скорости выполнения будет


def main_threads():
    tasks = []

    for i in range(n):
        tasks.append(threading.Thread(target=send_request, args=(i, URL)))  # создаем n потоков, указываем ф-ю к-я
        # будет запущена в потоке, и указываю аргументы в target ф-ю - send_request(i, URL). Это добавляем в tasks
        # пример - n кассовых линий и один кассир
        tasks[-1].start()  # стартуем каждый thread к-й я добавил

    # если бы не добавил что ниже, то функция main_threads закончилась бы раньше, чем выполнились бы все треды
    for task in tasks:
        task.join()  # проходимся по каждому потоку(таске) и указываем что нужно дождаться выполнения таски, а не
        # заканчивать функцию main_threads(главный поток)
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
# 3-й подход - asyncio. Конкурентность
# Появился с python 3.5. Стал стандартным с 3.7
# Работает в основном потоке, основан на работе генераторов
# await поход на yield


async def async_send_request(num: int, url: str, client: httpx.AsyncClient):
    print(f"Sending request #{num}")
    response = await client.get(url)
    print(response.status_code)


async def main_asyncio():
    async with httpx.AsyncClient() as client:  # создаем асинхронный клиент
        return await asyncio.gather(  # gather - множество карутин запускает в event.loop
            *[async_send_request(num, URL, client) for num in range(n)]  # создаем n карутин, передаем в gather
            # gather помещает в event.loop, они там крутятся, вытягиваются по одной таске и выполняются
            # выполнилась? - cообщаем. Нет? - заносим обратно в event.looop
        )



if __name__ == "__main__":
    start = time.perf_counter()
    # 50 запросов:

    # main_sync()  # 28.25 сек

    # main_threads()  # 0.72 сек. Запускаются в правильном порядке из-за tasks[-1].start()

    main_processes()  # 2.16 сек. Дольше, тут параллельность, а не конкурентность. Также нужно создать новый процесс,
    # выделить RAM, CPU, это всё требует времени.
    # Нет смысла создавать больше процессов чем ядер процессора.
    # Запуск неупорядоченный. Переключения между процессами на уровне ОС. Ей удобней было именно так отработать

    # asyncio.run(main_asyncio())  # 0.65 сек

    end = time.perf_counter()

    print("Elapsed", end - start)