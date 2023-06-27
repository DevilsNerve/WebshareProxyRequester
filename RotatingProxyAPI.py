import requests
import time
import random
from datetime import datetime, timedelta

# Configuration
api_key = 'YOUR_WEBSHARE_API_KEY'
target_url = 'TARGET_URL'
start_date = datetime.now()
end_date = start_date + timedelta(days=10)
total_requests = 10000

# Calculate sleep time
total_seconds = (end_date - start_date).total_seconds()
max_sleep_time = total_seconds / total_requests

# Proxies list to keep track of used proxies
used_proxies = set()

# Function to get a new proxy
def get_new_proxy():
    while True:
        try:
            response = requests.get(
                'https://proxy.webshare.io/api/proxy/list/',
                headers={'Authorization': f'Token {api_key}'}
            )
            proxies = response.json()['results']
            for proxy in proxies:
                if proxy['ip'] not in used_proxies:
                    used_proxies.add(proxy['ip'])
                    return {
                        'https': f'https://{proxy["username"]}:{proxy["password"]}@{proxy["ip"]}:{proxy["port"]}',
                        'http': f'http://{proxy["username"]}:{proxy["password"]}@{proxy["ip"]}:{proxy["port"]}'
                    }
        except:
            time.sleep(1)

# Main loop to send requests
elapsed_time = 0
for i in range(total_requests):
    proxy = get_new_proxy()
    
    try:
        response = requests.get(target_url, proxies=proxy, timeout=5)
        print(f'Request {i+1} - Status Code: {response.status_code}')
    except Exception as e:
        print(f'Request {i+1} failed - {str(e)}')

    sleep_time = random.uniform(0, max_sleep_time)
    elapsed_time += sleep_time
    remaining_time = total_seconds - elapsed_time

    # Adjust max_sleep_time for remaining requests
    remaining_requests = total_requests - (i + 1)
    if remaining_requests > 0:
        max_sleep_time = remaining_time / remaining_requests

    time.sleep(sleep_time)

print("Finished sending requests.")
