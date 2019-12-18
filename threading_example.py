# Situation: Evaluate web server performance against rapid spike in traffic (DoS attack)

import requests
import threading


def make_request():

    url = "https://www.ruqqus.com"
    response = requests.get(url)

    print(response.status_code)


def test_the_server(n=100):

    for i in range(n):
        new_thread = threading.Thread(target=make_request)
        new_thread.start()
