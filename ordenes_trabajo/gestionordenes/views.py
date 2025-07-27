from django.shortcuts import render
#from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from .models import OrdenTrabajo#, Cliente, EstadoOrden

def index(request):
    contexto = {
    'year': datetime.now().year,
    }
    return render(request, 'index.html', contexto)

def login(request):
    return render(request, 'login.html', {})

def register(request):
    return render(request, 'register.html', {})

@login_required
def odts(request):
    orden = OrdenTrabajo.objects.all()
    return render(request, 'odt.html', {'orden': orden})

def crear_orden(request):
    orden = OrdenTrabajo(
        odtTipoMaquina='Impresora',
        odtMarca='HP',
        odtModelo='LaserJet Pro M404dn',
        odtDescripcion='Descripción de la orden de trabajo 1',
        odtEstado='Pendiente',
        odtFecha='2023-10-01',
        odtNumero='ODT-003',
        odtFalla='Falla de la impresora',
    )
    orden.save()
    return render(request, 'crear_odt.html', {})

def detalle_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    return render(request, 'odt.html', {'orden': orden})

def editar_odt(request, odt_id):
    orden = OrdenTrabajo.objects.get(odtId=odt_id)
    return render(request, 'editar_odt.html', {'orden': orden})

def eliminar_odt(request, odt_id):
    context = {
        'odt_id': odt_id
    }
    return render(request, 'eliminar_odt.html', context)

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