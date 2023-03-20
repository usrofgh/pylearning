import functools


def benchmark(iters):
    def actual_decorator(func):
        import time
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print('[*] Среднее время выполнения: {} секунд.'.format(total / iters))
            return return_value

        return wrapper

    return actual_decorator


@benchmark(iters=2)
def fetch_webpage(url):
    'test'
    import requests
    webpage = requests.get(url)
    return webpage.text

print(fetch_webpage.__name__, fetch_webpage.__doc__)

webpage = fetch_webpage('https://google.com')
#print(webpage)