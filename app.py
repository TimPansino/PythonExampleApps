
import time

import falcon
import random

def respond(resp, text):
    resp.status = falcon.HTTP_200  # This is the default status
    resp.content_type = falcon.MEDIA_TEXT  # Default is JSON, so override
    resp.text = text

class RootRoute(object):
    def on_get(self, req, resp):
        respond(resp, "Hello from Falcon!")

class ErrorRoute(object):
    def on_get(self, req, resp):
        raise RuntimeError("Oops")

class SpottyRoute(object):
    def on_get(self, req, resp):
        if random.randint(1, 5) == 5:
            raise RuntimeError("Oops")
        else:
            respond(resp, "Hello from Falcon!")

class SlowRoute(object):
    def on_get(self, req, resp):
        time.sleep(5)
        respond(resp, "Hello from Falcon! (slowly)")


app = falcon.App()
app.add_route("/", RootRoute())
app.add_route("/error", ErrorRoute())
app.add_route("/spotty", SpottyRoute())
app.add_route("/slow", SlowRoute())
