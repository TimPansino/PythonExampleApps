from django.shortcuts import render

# Create your views here.

def index(request):
    absolute_url = request.build_absolute_uri().rstrip("/")
    return render(request, "channelsdemo/index.html", {"absolute_url": absolute_url})
