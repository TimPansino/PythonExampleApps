from flask import Flask
import random
import time

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/error')
def error():
    raise RuntimeError("Oops")


@app.route('/spotty')
def spotty():
    if random.randint(1, 5) == 5:
        raise RuntimeError("Oops")
    else:
        return "Hello from Flask!"

@app.route('/slow')
def slow():
    time.sleep(5)
    return "Hello from Falcon! (slowly)"


if __name__ == '__main__':
    app.run(port=8000)
