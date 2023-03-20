import asyncio
import time
import httpx  # поддерживает async под капотом
from bs4 import BeautifulSoup
from httpx import AsyncClient

URL = "https://djinni.co/jobs/?primary_keyword=Python/"


def get_djinni_jobs(page: int):
    response = httpx.get(URL, params={"page": page})
    soup = BeautifulSoup(response.content, "html.parser")
    return [job.text.strip() for job in soup.select(".profile")]


def main():
    for page in range(1, 15):
        print(get_djinni_jobs(page))


async def async_get_djinni_jobs(page: int, client: AsyncClient):
    response = await client.get(URL, params={"page": page})
    soup = BeautifulSoup(response.content, "html.parser")
    return [job.text.strip() for job in soup.select(".profile")]


async def amain():
    async with AsyncClient() as client:
        jobs_pages = await asyncio.gather(*[async_get_djinni_jobs(page, client) for page in range(0, 56 + 1)])
    for jobs in jobs_pages:
        print(jobs)

if __name__ == '__main__':
    start_time = time.perf_counter()
    asyncio.run(amain())
    end_time = time.perf_counter()
    print("Elapsed:", end_time - start_time)
    # 5.7 sec. - sync
    # 0.93 sec. - asyncio