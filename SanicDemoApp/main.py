from sanic import Sanic
from sanic.response import json
import random
import time

app = Sanic(__name__)

def respond(text):
    return json({"text": text})

@app.route('/')
def hello(request):
    return respond("Hello from Sanic!")

@app.route('/error')
def error(request):
    raise RuntimeError("Oops")


@app.route('/spotty')
def spotty(request):
    if random.randint(1, 5) == 5:
        raise RuntimeError("Oops")
    else:
        return respond("Hello from Sanic!")

@app.route('/slow')
def slow(request):
    time.sleep(5)
    return respond("Hello from Sanic! (slowly)")


if __name__ == '__main__':
    app.run(port=8000)
