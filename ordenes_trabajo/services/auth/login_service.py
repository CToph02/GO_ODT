from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def Log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)
    print(f"User authenticated: {user}")

    if user is not None:
        login(request, user)
        return redirect('odts')
    return render(request, 'login.html', {})

def Log_out(request):
    logout(request)
    return redirect('index')