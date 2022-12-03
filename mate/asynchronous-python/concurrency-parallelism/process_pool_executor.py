import multiprocessing
import time

from concurrent.futures import ProcessPoolExecutor, wait

n = 10


def sum_up_elems_with_3(start: int, end: int):
    print(sum(num for num in range(start, end + 1) if "3" in str(num)))


def main_process():
    tasks = []

    for i in range(n):
        tasks.append(multiprocessing.Process(target=sum_up_elems_with_3, args=(i * 1_000, i * 1_000_000)))
        tasks[-1].start()  # сами стартуем

    for task in tasks:
        task.join()  # сами джоиним


def main_pool_executor():
    futures = []

    # создаем столько процессов, сколько есть ядер и не больше чем нужно
    with ProcessPoolExecutor(multiprocessing.cpu_count() - 1) as executor:
        for i in range(n):  # теперь если n == 100, то не будет создаваться 100 процессов.
            # А будет создаваться ровно столько, сколько есть ядер
            futures.append(executor.submit(sum_up_elems_with_3, i * 1_000, i * 1_000_000))

    wait(futures)  # дожидаюсь того, когда выполнятся все внесенные задачи


if __name__ == "__main__":
    start_time = time.perf_counter()
    main_pool_executor()  # 1.58

    # for i in range(n):
    #     sum_up_elems_with_3(i * 1_000, i * 1_000_000)  # 6.54

    end_time = time.perf_counter()
    print("Elapsed: ", end_time - start_time)  # 1.55 sec. Скорость такая же, просто реализация проще
    # также есть и ThreadPoolExecutor, но чаще встречается ProcessPoolExecutor