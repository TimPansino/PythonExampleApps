from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "chatasync/index.html")

def room(request, room_name):
    return render(request, "chatasync/room.html", {"room_name": room_name})
