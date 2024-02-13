from django.shortcuts import render, redirect

# importer les models
from .models import *

# Create your views here.

# function to display home.html
def home(request):
    return render(request, 'home.html')

# function to display room.html
def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
    })

# function permettant de vérifier les informations que l'utilisateur a entré dans le formulaire du home.html, l'on récupère les informations par la méthode POST
def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    
    # vérifie si le room_name entré par l'utilisateur existe 
    if Room.objects.filter(name = room).exists():
        return redirect('/'+ room + '/?username' + username)
    else:
        new_room = Room.objects.create(name = room)
        new_room.save()
        return redirect('/'+ room + '/?username' + username) 
        
