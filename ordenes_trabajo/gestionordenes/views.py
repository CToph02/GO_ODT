from django.shortcuts import render, redirect
#from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import AuthenticationForm
from .models import OrdenTrabajo#, Cliente, EstadoOrden
from django.db.models import Q

def index(request):
    contexto = {
    'year': datetime.now().year,
    }
    return render(request, 'index.html', contexto)

def log_in(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    print(f"Username: {username}, Password: {password}")
    user = authenticate(username=username, password=password)
    print(f"User authenticated: {user}")
    if user is not None:
        login(request, user)
        return redirect('odts')
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

def log_out(request):
    logout(request)
    return redirect('index')

@login_required
def odts(request):
    orden = OrdenTrabajo.objects.all()
    return render(request, 'odt.html', {'orden': orden})

def crear_odt(request):
    if request.method == 'POST':
        # Datos Cliente
        clientName = request.POST.get('client_name')
        clientPhone = request.POST.get('client_number')
        clientEmail = request.POST.get('client_email')
        clientAddress = request.POST.get('client_address')
        # Datos ODT
        #odtNumero = request.POST.get('serial_number')
        marca = request.POST.get('brand')
        modelo = request.POST.get('model')
        tipo_maquina = request.POST.get('type_machine')
        marca = request.POST.get('brand')
        modelo = request.POST.get('model')
        falla = request.POST.get('fault')
        metodoPago = request.POST.get('odtPaymentForm')
        diagnostico = request.POST.get('diagnosticpay')
        recepcion = request.POST.get('recepcion')

        print(diagnostico)

        orden = OrdenTrabajo(
            odtClientName=clientName,
            odtClientPhone=clientPhone,
            odtClientEmail=clientEmail,
            odtClientAddress=clientAddress,
            #odtDescripcion='',
            odtEstado='Pendiente',
            odtModelo=modelo,
            odtMarca=marca,
            odtFalla=falla,
            odtTipoMaquina=tipo_maquina,
            odtPaymentForm=metodoPago,
            odtDiagnostico=diagnostico,
            odtRecepcion=recepcion
        )
        orden.save()
    return redirect('odts')

def detalle_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    return render(request, 'odt.html', {'orden': orden})

def editar_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    return render(request, 'editar_odt.html', {'orden': orden})

def eliminar_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    orden.delete()
    return redirect('odts')

def imprimir_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    return render(request, 'imprimir.html', {'orden': orden})

def buscar_odt(request):
    if request.method == 'POST':
        query = request.POST.get('search')
        if query:
            orden = OrdenTrabajo.objects.filter(
                Q(odtId__icontains=query) | 
                Q(odtClientName__icontains=query) | 
                Q(odtClientPhone__icontains=query))
        else:
            orden = OrdenTrabajo.objects.all()
    return render(request, 'odt.html', {'orden': orden})
    # query = request.GET.get('query')
    # if query:
    #     ordenes = OrdenTrabajo.objects.filter(odtNumero__icontains=query)
    # else:
    #     ordenes = OrdenTrabajo.objects.all()
    # return render(request, 'odt.html', {'orden': ordenes})

def actualizar_estado_odt(request, odt_id):
    context = {
        'odt_id': odt_id,
        'new_status': 'Completada'  # Example status update
    }
    return render(request, 'actualizar_estado_odt.html', context)

def estado(request):
    context = {
        'odt_id': "odt_id",
        'status': 'Pendiente'  # Example status
    }
    return render(request, 'estado.html', context)