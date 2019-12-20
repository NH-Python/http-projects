import os
import requests
from pprint import pprint


def do_gets():
    resp = requests.get("https://httpbin.org/get")
    pprint(resp.json())
    print(f"Status Code: {resp.status_code}")

    # resp = requests.get("https://httpbin.org/get", params={"p1": "value", "p2": "This Has #Characters that ^!& need to be ? escaped"})
    # pprint(resp.json())

    # # Sending a GET to an endpoint that only supports POST...
    # # ... We expect this to return a non-success error code
    # resp = requests.get("https://httpbin.org/post")
    # print(f"Status Code: {resp.status_code}")


def do_posts():
    ## don't post any data
    resp = requests.post("https://httpbin.org/post")
    pprint(resp.json())
    print(f"Status Code: {resp.status_code}")

    ## post form data
    # resp = requests.post("https://httpbin.org/post", data={"field1": "value 1", "field2": 999, "field3": "$Does this need to be & escaped ???"})
    # pprint(resp.json())

    ## post json data
    # resp = requests.post("https://httpbin.org/post", json={"field1": "value 1", "field2": 999, "field3": "$Does this need to be & escaped ???"})
    # pprint(resp.json())

    ## post a file
    # files = {'file': open(os.path.abspath(__file__), 'r')}
    # resp = requests.post("https://httpbin.org/post", files=files)
    # pprint(resp.json())

    ## request.post doesn't give us a params keyword argument, but we can use a prepared request
    ## to get that functionality if we need it
    # r = requests.Request(method="POST")
    # r.url = "https://httpbin.org/post"
    # r.params = { "p1": "value", "p2": 33, "param3": "Escape ?&%%%"}
    # r.data = {"field1": "val1", "field2": "val2"}
    # prepared = r.prepare()
    # with requests.Session() as s:
    #     resp = s.send(prepared)
    #     pprint(resp.json())


if __name__ == "__main__":
    do_gets()
    # do_posts()
