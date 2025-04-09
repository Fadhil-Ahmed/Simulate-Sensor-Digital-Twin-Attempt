import requests
import random
import time

LOG_URL = "http://127.0.0.1:8000/log_sensor_data"
STATUS_URL = "http://127.0.0.1:8000/status"

while True:
    try:
        # Check robot status
        status_response = requests.get(STATUS_URL).json()
        if status_response["status"] == "start":
            # Only log data if robot is 'start'
            value = round(random.uniform(10.0, 30.0), 2)
            response = requests.post(LOG_URL, json={"value": value})
            print(f"Sent: {value} | Response: {response.json()}")
        else:
            print("Robot is stopped. No data sent.")
    except Exception as e:
        print("Error:", e)

    time.sleep(2)
