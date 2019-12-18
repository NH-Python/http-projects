import requests
from os import environ
from urllib.parse import urlparse

from .get import *
from ruqqus.__main__ import db

def thumbnail_thread(post):

    params={"access_key":environ.get("APIFLASH_KEY"),
            "url": post.url,
            "height":720,
            "width":1280,
            "format":"jpeg",
            "response_type":"json",
            "thumbnail_width":300
            }


    x=requests.get("https://api.apiflash.com/v1/urltoimage", params=params)

    post.thumb_id=urlparse(x.json()["url"]).path.split("/")[-1].split(".")[0]

    db.add(post)
    db.commit()


#============
    
@app.route("/submit", methods=["POST"])
def submit_post():

    # [processing, validation, etc]
    
    #spin off thumbnail generation as  new thread
    if new_post.url and not new_post.url.endswith((".jpeg",".jpg",".png")):
        new_thread=threading.Thread(target=thumbnail_thread, args=(new_post,))
        new_thread.start()

    #continue processing new post stuff
    #eventually returns 301 to new post link
