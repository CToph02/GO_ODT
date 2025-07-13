from django.shortcuts import render
from datetime import datetime
# Create your views here.

def index(request):
    contexto = {
    'year': datetime.now().year,
    }
    return render(request, 'index.html', contexto)

def login(request):
    return render(request, 'login.html', {})

def signup(request):
    return render(request, 'signup.html', {})

def odts(request):
    return render(request, 'odts.html', {})