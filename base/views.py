from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm


#Create your views here.

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    print('hola')
    form = RoomForm()
    if request.method == "POST":
        print("hijo de su perra madre")
        print(request.POST)
        #print('hijo de perra')
        #form = RoomForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)


