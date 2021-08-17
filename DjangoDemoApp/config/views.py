from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello World!")


def crash(request):
    raise ValueError()
