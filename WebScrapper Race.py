import urllib
import multiprocessing
import asyncio
import threading
import time
import aiohttp
from bs4 import BeautifulSoup as bs


# Function to fetch data from 
def fetch_data(url):
    response = urllib.request.urlopen(url)
    webpage = response.read()
    soup = bs(webpage, 'html.parser')
    books = soup.find_all('article', class_='product_pod')
    return len(books)

async def fetch_data_async(url, session):
    async with session.get(url) as response:
        webpage = await response.read()
        soup = bs(webpage, 'html.parser')
        return len(soup.find_all('article', class_='product_pod'))

def run_threads(url, count):
    threads = []
    for i in range(count):
        t = threading.Thread(target=fetch_data, args=(url,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def run_processes(url, count):
    processes = []
    for i in range(count):
        p = multiprocessing.Process(target=fetch_data, args=(url,))
        processes.append(p)
        p.start()
    for p in processes:
        p.join()

async def run_async(url, count):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data_async(url, session) for _ in range(count)]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    target_url = "https://books.toscrape.com/catalogue/category/books/horror_31/index.html"
    num_runs = 5

    # 1. Test Multiprocessing
    start = time.perf_counter()
    run_processes(target_url, num_runs)
    print(f"Multiprocessing took: {time.perf_counter() - start:.2f} seconds")

    # 2. Test Multithreading
    start = time.perf_counter()
    run_threads(target_url, num_runs)
    print(f"Multithreading took: {time.perf_counter() - start:.2f} seconds")

    # 3. Test Asyncio
    start = time.perf_counter()
    asyncio.run(run_async(target_url, num_runs))
    print(f"Asyncio took: {time.perf_counter() - start:.2f} seconds")