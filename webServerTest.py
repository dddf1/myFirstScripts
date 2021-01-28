#Rafi Maman

import requests
from requests.auth import HTTPBasicAuth

url = "http://localhost:8000/players?"


def false_authentication():
    response = requests.get(url,
                            auth=HTTPBasicAuth("admin", "aaa"),
                            params={"page": "1"})

    if response.status_code != 200:
        print("PASSED - Negative credentials testing")
    else:
        print("***** TEST FAILED ***** Something is wrong if status is 200. STATUS YOU GET IS : " + format(response.status_code))


def content():
    x = 0
    while x <= 20:
        x += 1
        response = requests.get(url ,
                                auth =HTTPBasicAuth("admin", "admin"),
                                params = {"page":x})
        data = response.text
        if "null" in data:
            print(data)
            return print(f"***** TEST FAILED ***** Invalid data in page: {x}")
    print("PASSED - No invalid data found")


false_authentication()
content()