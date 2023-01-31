import newrelic.agent

import time

from flask import Flask


app = Flask(__name__)


@app.route('/')
def root():
    keep_span()
    send_spans()
    return "Hello from Flask!"


@newrelic.agent.function_trace()
def send_spans(n=20):
    """Generate n spans recursively for testing infinite tracing."""
    keep_span()
    n -= 1
    if n:
        send_spans(n)
    else:
        time.sleep(1)


def keep_span():
    newrelic.agent.add_custom_span_attribute("keepTrace", True)


if __name__ == '__main__':
    app.run(port=8000)
