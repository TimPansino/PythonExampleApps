from django.http import HttpResponse
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
