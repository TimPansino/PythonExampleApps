from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello from Flask!"

@app.route('/error')
def error():
    raise RuntimeError("Oops")

if __name__ == '__main__':
    app.run(port=8000)
