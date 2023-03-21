from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

rooms = [
    {'id':1, 'name':'Margarita'},
    {'id':2, 'name':'Dry mattini'},
    {'id':3, 'name':'Espresso'},
]

abouts = [
    {'id':7, 'name':'hfghg'},
    {'id':8, 'name':'ghgfh'},
    {'id':9, 'name':'fghh'},
]

def home(request):
    context = {'rooms': rooms, 'abouts':abouts}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'rooms': room} 
    return render(request, 'base/room.html', context)


def about(request, pk):
    about = None
    for j in abouts:
        if j["id"] == int(pk):
            about = j
    context = {'abouts': about}
    return render(request, 'base/about.html', context)