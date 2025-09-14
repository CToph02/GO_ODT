from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import OrdenTrabajo#, Cliente, EstadoOrden
from django.db.models import Q
from services.auth.login_service import Log_in, Log_out
from services.auth.register_service import reg

#from django.http import HttpResponse
#from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')

def log_in(request):
    return Log_in(request)

def log_out(request):
    return Log_out(request)

def register(request):
    return reg(request)

@login_required
def odts(request):
    orden = OrdenTrabajo.objects.all()
    return render(request, 'odt.html', {'orden': orden})

@login_required
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
        #recepcionadoPor = request.POST.get('')

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

@login_required
def detalle_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    return render(request, 'odt.html', {'orden': orden})

@login_required
def editar_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    return render(request, 'editar_odt.html', {'orden': orden})

@login_required
def eliminar_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    orden.delete()
    return redirect('odts')

@login_required
def imprimir_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    return render(request, 'imprimir.html', {'orden': orden})

@login_required
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

@login_required
def actualizar_estado_odt(request, odt_id):
    context = {
        'odt_id': odt_id,
        'new_status': 'Completada'
    }
    return render(request, 'actualizar_estado_odt.html', context)

@login_required
def estado(request):
    context = {
        'odt_id': "odt_id",
        'status': 'Pendiente'
    }
    return render(request, 'estado.html', context)