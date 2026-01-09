import os
from flask import Flask
from redis import Redis

app = Flask(__name__)
redis_host = os.getenv('REDIS_HOST', 'redis')
redis = Redis(host=redis_host, port=6379)

@app.route('/')
def hello():
    count = redis.incr('hits')
    return f'<h1>DevOps Project 2</h1><p>This page has been viewed {count} times.</p>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)