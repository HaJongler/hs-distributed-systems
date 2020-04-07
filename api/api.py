import hashlib

import redis
from flask import Flask

app = Flask(__name__)
redis_conn = redis.from_url("redis://redis:6379")


@app.route("/")
def index():
    return "Usage: " \
           "To shorten your link use: http://<hostname>[:<prt>]/put/<url>. " \
           "To find the real url behind a short link use: http://<hostname>[:<prt>]/get/<url>."


@app.route("/get/<short_url>")
def get_long_link(short_url):
    long_link = redis_conn.get(short_url)
    return long_link if long_link else "This short URL doesn't exist in the system."


@app.route("/put/<long_url>")
def get_short_link(long_url):
    short_link = redis_conn.get(long_url)
    if short_link is None:
        sha = hashlib.sha1()
        sha.update(long_url.encode())
        short_link = f'https://jonathan-urls/{sha.hexdigest()[:8]}'
        redis_conn.set(long_url, short_link)
        redis_conn.set(short_link, long_url)
    return short_link


app.run(host="0.0.0.0", port=5000)
