import time
import httpx

URL = "https://www.google.com/"

n = 10


def send_request(num: int, url: str):
    print(f"sending request #{num}")
    response = httpx.get(url)
    print(response.status_code)


def main_async():
    for i in range(n):
        send_request(i, URL)


if __name__ == "__main__":
    start = time.perf_counter()
    main_async()
    end = time.perf_counter()
    print("Elapsed: ", end - start)




