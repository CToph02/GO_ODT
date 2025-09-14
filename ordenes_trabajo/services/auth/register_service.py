from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import render, redirect

def reg(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')

        if not username or not email or not password or not password:
            messages.error(request, "Por favor, complete todos los campos")
            return redirect("register")

        if password != password2:
            messages.error(request, "Las contraseñas no coinciden")
            return redirect("register")
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "El nombre de usuario ya existe")
            return redirect("register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Ya existe una cuenta con este correo electrónico")

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()

        login(request, user)

        messages.success(request, "Usuario registrado exitosamente")
        return redirect('index')
    
    return render(request, 'register.html', {})