import asyncio, time, requests, httpx

def get_response_id(url):
    response = requests.get(url)
    response_id =  response.headers.get("x-amzn-requestid","No Request ID")
    return response_id

async def async_get_response_id(url):
    response = await httpx.AsyncClient().get(url)
    response_id = response.headers.get("x-amzn-requestid","No Request ID")
    return response_id


async def gather_responses(urls):
    tasks = [async_get_response_id(url) for url in urls]
    results = await asyncio.gather(*tasks)
    return results

if __name__=="__main__":
    url="https://fakeresponder.com/?sleep=2000"
    
    print("Sending a single http request that takes 2 seconds to complete.")
    start = time.time()
    response_id = get_response_id(url)
    end = time.time()
    print(f"Response ID: {response_id}")
    print(f"Took {end - start:.2f} seconds.\n")

    # Any function that has async in front of it must be called with asyncio.run()
    print("Now sending the same request, but with an async call. There is really no point to doing this if there is only one.")
    start = time.time()
    response_id = asyncio.run(async_get_response_id(url))
    end = time.time()
    print(f"Response ID: {response_id}")
    print(f"Took {end - start:.2f} seconds.\n")

    # The key part of async is using an asyncio.gather() call to send multiple async requests at once.
    print("The real reason to use async is to send off multiple requests at once and not have to wait for one to finish before sending the next.")
    print("Now sending 10 http requests that each take 2 seconds to complete.")
    print("Sending them asynchronously so they all complete in about 2 seconds.")
    start = time.time()
    response_ids = asyncio.run(gather_responses([url]*10))
    end = time.time()
    for id in response_ids:
        print(f"Response ID: {id}")
    print(f"Took {end - start:.2f} seconds.\n")

    print("Now sending the same 10 requests, but synchronously.")
    print("This takes about 20 seconds because we have to wait for each to return before advancing to the next line of code.")
    start = time.time()
    for url in [url]*10:
        response_id = get_response_id(url)
        print(f"Response ID: {response_id}")
    end = time.time()
    print(f"Took {end - start:.2f} seconds.\n")
  