import asyncio
from datetime import time, datetime

import aiohttp

async def fetch_data(session, url):
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer access_token'
    }
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            data = await response.json()
        else:
            return f'Error: {response.status}'

async def main(should_return=False):
    num_iteration = 2000
    url = 'http://127.0.0.1:5000/retrieve-transactions'
    print(f'Executing REST API call in async.py to {url} for {num_iteration} iterations ')

    start_time = datetime.now()
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(session, url) for _ in range(num_iteration)]
        await asyncio.gather(*tasks)
        if should_return:
            return await asyncio.gather(*tasks)

    end_time = datetime.now()
    print(f'Total Execution Time for async.py: {end_time - start_time} seconds')


if __name__ == '__main__':
    asyncio.main()