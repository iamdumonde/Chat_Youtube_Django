from django.shortcuts import render, redirect
from django.http import HttpResponse
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
        'room_details': room_details, #c'est un objet, l'ensemble formé par le nom et l'id du room
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
        

# la fonction send s'occupera d'envoyer les messages
def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']
    
    new_message = Message.objects.create(value = message, user = username, room = room_id)
    new_message.save()
    return HttpResponse('Message envoyé avec succès')