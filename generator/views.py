from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    passis = 'testing'
    characters = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length', 12))
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))
    thepassword = ''
    for x in range(length):
        thepassword += characters[int(round(random.random()*len(characters)-1))] #or use random.choice(characters)
    return render(request, 'generator/password.html', {'password':thepassword})
    # return render(request, 'generator/password.html', {'password': passis})

def about(request):
    return render(request, 'generator/about.html') 
