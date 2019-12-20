import requests
from werkzeug.exceptions import Aborter


def raise_404_exception():
    r = requests.get("https://httpbin.org/nope")
    if r.status_code != 200:
        Aborter()(code=r.status_code)
    print("this won't print")


def dont_raise_404_exception():
    r = requests.get("https://httpbin.org/get")
    if r.status_code != 200:
        Aborter()(code=r.status_code)
    print("this will print")


if __name__ == "__main__":
    dont_raise_404_exception()
    raise_404_exception()
