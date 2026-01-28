from datetime import time, datetime
import requests


def main(should_return=False):
    obj = []
    num_iteration = 2000
    url = 'http://127.0.0.1:5000/retrieve-transactions'
    print(f'Executing REST API call in non_async.py to {url} for {num_iteration} iterations ')

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer access_token'
    }
    start_time = datetime.now()
    for i in range(num_iteration):
        r = requests.get(url, headers=headers)
        obj.append(r.json())
    end_time = datetime.now()
    print(f'Total Execution Time for non_async.py: {end_time - start_time} seconds')

    if should_return:
        return obj
    return None


if __name__ == '__main__':
    main()