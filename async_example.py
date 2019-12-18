import asyncio
import httpx
from pprint import pprint


async def do_gets():
    resp = await httpx.get("https://httpbin.org/get")
    pprint(resp.json())
    print(f"Status Code: {resp.status_code}")
    return resp


async def do_posts():
    # don't post any data
    resp = await httpx.post("https://httpbin.org/post")
    pprint(resp.json())
    print(f"Status Code: {resp.status_code}")


if __name__ == "__main__":
    asyncio.run(do_gets())
    asyncio.run(do_posts())
