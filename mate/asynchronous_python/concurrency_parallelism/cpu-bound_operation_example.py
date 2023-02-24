import asyncio
import multiprocessing
import threading
import time

n = 10

# CPU-bound operations - любые арифметические операции


def sum_up_elems_with_3(start: int, end: int):
    print(sum(num for num in range(start, end + 1) if "3" in str(num)))


async def async_sum_up_elems_with_3(start: int, end: int):
    print(sum(num for num in range(start, end + 1) if "3" in str(num)))


def main_sync():
    for i in range(n):
        sum_up_elems_with_3(i * 1_000, i * 1_000_000)


def main_threads():
    tasks = []

    for i in range(n):
        tasks.append(threading.Thread(target=sum_up_elems_with_3, args=(i * 1_000, i * 1_000_000)))
        tasks[-1].start()

    for task in tasks:
        task.join()


def main_processes():
    tasks = []

    for i in range(n):
        tasks.append(multiprocessing.Process(target=sum_up_elems_with_3, args=(i * 1_000, i * 1_000_000)))
        tasks[-1].start()

    for task in tasks:
        task.join()


async def main_asyncio():
    return await asyncio.gather(
        *[async_sum_up_elems_with_3(i * 1_000, i * 1_000_000) for i in range(n)]
    )

if __name__ == "__main__":
    s = time.perf_counter()
    # main_sync()  # 6.69 sec

    # main_threads() # 6.41 sec - разницы нет с синхронным. Так как тут нет I/O bound. Конкурентность не нужна.
    # На других ядрах нельзя запустить потоки из-за GIL

    # asyncio.run(main_asyncio())  # 6.52 sec. asyncio конкретный, поскольку cpu-bound, конкурентность тут не нужна

    # main_processes()  # 1.60 sec. Параллельность, расчеты действительно одновременно были на разных ядрах процессора
    e = time.perf_counter()
    print("Elapsed: ", e - s)