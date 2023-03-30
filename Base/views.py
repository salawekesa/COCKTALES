from django.shortcuts import render
from django.http import HttpResponse
from .models import Room

# Create your views here.

# rooms = [
#     {'id':1, 'name':'Margarita'},
#     {'id':2, 'name':'Dry mattini'},
#     {'id':3, 'name':'Espresso'},
# ]

abouts = [
    {'id':7, 'name':'hfghg'},
    {'id':8, 'name':'ghgfh'},
    {'id':9, 'name':'fghh'},
]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms, 'abouts':abouts}
    return render(request, 'Base/home.html', context)

def room(request, pk):
    rooms = Room.objects.get(id=pk)
    context = {'rooms': rooms} 
    return render(request, 'Base/room.html', context)


def about(request, pk):
    about = None
    for j in abouts:
        if j["id"] == int(pk):
            about = j
    context = {'abouts': about}
    return render(request, 'Base/about.html', context)