import requests
import time
import random

API_URL = "http://api-service:5000"

while True:
    try:
        r = requests.get(API_URL)
        print("Request sent:", r.status_code)
    except Exception as e:
        print("Error:", e)

    time.sleep(random.uniform(0.1, 0.5))
