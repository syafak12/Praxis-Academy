# import requests
# import time


# def download_site(url, session):
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with requests.Session() as session:
#         for url in sites:
#             download_site(url, session)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")


# download di terminal:
# $ ./io_non_concurrent.py
#    [most output skipped]
# Downloaded 160 in 14.289619207382202 seconds


# import concurrent.futures
# import requests
# import threading
# import time


# thread_local = threading.local()


# def get_session():
#     if not hasattr(thread_local, "session"):
#         thread_local.session = requests.Session()
#     return thread_local.session


# def download_site(url):
#     session = get_session()
#     with session.get(url) as response:
#         print(f"Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         executor.map(download_site, sites)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")




# thread_local = threading.local()


# def get_session():
#     if not hasattr(thread_local, "session"):
#         thread_local.session = requests.Session()
#     return thread_local.session




# download di terminal:
# $ ./io_threading.py
#    [most output skipped]
# Downloaded 160 in 3.7238826751708984 seconds



# import asyncio
# import time
# import aiohttp


# async def download_site(session, url):
#     async with session.get(url) as response:
#         print("Read {0} from {1}".format(response.content_length, url))


# async def download_all_sites(sites):
#     async with aiohttp.ClientSession() as session:
#         tasks = []
#         for url in sites:
#             task = asyncio.ensure_future(download_site(session, url))
#             tasks.append(task)
#         await asyncio.gather(*tasks, return_exceptions=True)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     asyncio.get_event_loop().run_until_complete(download_all_sites(sites))
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} sites in {duration} seconds")



# download di terminal:
# $ ./io_asyncio.py
#    [most output skipped]
# Downloaded 160 in 2.5727896690368652 seconds



# import requests
# import multiprocessing
# import time

# session = None


# def set_global_session():
#     global session
#     if not session:
#         session = requests.Session()


# def download_site(url):
#     with session.get(url) as response:
#         name = multiprocessing.current_process().name
#         print(f"{name}:Read {len(response.content)} from {url}")


# def download_all_sites(sites):
#     with multiprocessing.Pool(initializer=set_global_session) as pool:
#         pool.map(download_site, sites)


# if __name__ == "__main__":
#     sites = [
#         "https://www.jython.org",
#         "http://olympus.realpython.org/dice",
#     ] * 80
#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f"Downloaded {len(sites)} in {duration} seconds")



# di terminal:
# $ ./io_mp.py
#     [most output skipped]
# Downloaded 160 in 5.718175172805786 seconds



# def cpu_bound(number):
#     return sum(i * i for i in range(number))


# import time


# def cpu_bound(number):
#     return sum(i * i for i in range(number))


# def find_sums(numbers):
#     for number in numbers:
#         cpu_bound(number)


# if __name__ == "__main__":
#     numbers = [5_000_000 + x for x in range(20)]

#     start_time = time.time()
#     find_sums(numbers)
#     duration = time.time() - start_time
#     print(f"Duration {duration} seconds")


# di terminal:
# $ ./cpu_non_concurrent.py
# Duration 7.834432125091553 seconds

# di terminal:
# $ ./cpu_threading.py
# Duration 10.407078266143799 seconds


# import multiprocessing
# import time


# def cpu_bound(number):
#     return sum(i * i for i in range(number))


# def find_sums(numbers):
#     with multiprocessing.Pool() as pool:
#         pool.map(cpu_bound, numbers)


# if __name__ == "__main__":
#     numbers = [5_000_000 + x for x in range(20)]

#     start_time = time.time()
#     find_sums(numbers)
#     duration = time.time() - start_time
#     print(f"Duration {duration} seconds")


# di terminal:
# $ ./cpu_mp.py
# Duration 2.5175397396087646 seconds







