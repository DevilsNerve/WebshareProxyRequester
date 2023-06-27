# Webshare Proxy Requester

This script allows you to send HTTP requests to a target URL through different proxies retrieved from Webshare.io over a period of time. It is especially useful for scenarios where you need to send a large number of requests to a target URL without hitting rate limits or to simulate traffic from different IPs.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)
- [Contribute](#contribute)
- [Contact](#contact)

## Features
- Fetch proxies from Webshare.io
- Send HTTP requests through different proxies to a target URL
- Spread requests over a specific period of time
- Customizable total number of requests

## Prerequisites
- Python 3.6+
- requests library
- A Webshare.io account and API Key

## Installation
To install the requests library, use pip:
```
pip install requests
```

## Usage
1. Clone this repository:
```
git clone https://github.com/your-repo/webshare-proxy-requester.git
```

2. Change to the directory:
```
cd webshare-proxy-requester
```

3. Edit the script and set your Webshare API key, target URL, start date, end date, and total number of requests:
```python
api_key = 'YOUR_WEBSHARE_API_KEY'
target_url = 'TARGET_URL'
start_date = datetime.now()
end_date = start_date + timedelta(days=10)
total_requests = 10000
```

4. Run the script:
```
python script.py
```

## License
This code is licensed under the **Custom Commercial Royalty License**. You are free to use, modify, distribute the code, but if you are using it commercially, the owner should be paid a royalty fee. Details of the royalty fee and how it should be paid can be discussed with the owner. For more details, please refer to the LICENSE file.

## Contribute
Contributions, issues, and feature requests are welcome. Feel free to check issues page if you want to contribute.

## Contact
GitHub repository: [https://github.com/your-repo/webshare-proxy-requester](https://github.com/your-repo/webshare-proxy-requester)
Email: admin@devilsnerve.com
Please make sure to update tests as appropriate.

---

© Copyright Devils Nerve, All rights reserved.
