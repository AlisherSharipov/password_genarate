from django.shortcuts import render
import random
# Create your views here.
def home(request):
    return render(request, 'generate\home.html')
def password(request):
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    thepassword = ''
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNOPQRSTUWXYZ')
    if request.GET.get('numbers'):
        characters.extend('0123456789')
    if request.GET.get('symbol'):
        characters.extend('!@#$%')
    for i in range(length):
        thepassword += random.choice(characters)
    return render(request, 'generate\password.html', {'password': thepassword})



