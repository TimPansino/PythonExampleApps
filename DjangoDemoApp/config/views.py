from django.http import HttpResponse
from django.views import View
import time
import random


def index(request):
    return HttpResponse("Hello from Django!")


def error(request):
    raise RuntimeError("Oops")

def spotty():
    if random.randint(1, 5) == 5:
        raise RuntimeError("Oops")
    else:
        return HttpResponse("Hello from Django!")

def slow():
    time.sleep(5)
    return HttpResponse("Hello from Django! (slowly)")

class IndexView(View):
    def get(self, request):
        return HttpResponse("Hello from Django!")


class ErrorView(View):
    def get(self, request):
        raise RuntimeError("Oops")

class SpottyView(View):
    def get(self, request):
        if random.randint(1, 5) == 5:
            raise RuntimeError("Oops")
        else:
            return HttpResponse("Hello from Django!")

class SlowView(View):
    def get(self, request):
        time.sleep(5)
        return HttpResponse("Hello from Django! (slowly)")
