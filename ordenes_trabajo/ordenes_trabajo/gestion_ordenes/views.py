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
    context = {
        'odts':[
            {
                'id': 1,
                'typeMachine': 'Impresora',
                'clientName': 'Christopher Muñoz',
                'brand': 'HP',
                'model': 'LaserJet Pro M404dn',
                'celNum': '1234567890',
                'description': 'Descripción de la orden de trabajo 1',
                'status': 'Pendiente',
                'created_at': '2023-10-01',
                'assigned_to': 'Usuario 1'
            },
            {
                'id': 2,
                'typeMachine': 'Plotter',
                'brand': 'Canon',
                'model': 'imagePROGRAF PRO-1000',
                'clientName': 'Ana Pérez',
                'celNum': '0987654321',
                'description': 'Descripción de la orden de trabajo 2',
                'status': 'En Proceso',
                'created_at': '2023-10-02',
                'assigned_to': 'Usuario 2'
            },
            {
                'id': 3,
                'typeMachine': 'Impresora',
                'brand': 'Brother',
                'model': 'HL-L8360CDW',
                'clientName': 'Luis Gómez',
                'celNum': '1122334455',
                'description': 'Descripción de la orden de trabajo 3',
                'status': 'Completada',
                'created_at': '2023-10-03',
                'assigned_to': 'Usuario 3'
            }
        ]
    }
    return render(request, 'odt.html', context)

def crear_odt(request):
    return render(request, 'crear_odt.html', {})

def detalle_odt(request, odt_id):
    context = {
        'odt': {
            'id': odt_id,
            'typeMachine': 'Impresora',
            'clientName': 'Christopher Muñoz',
            'brand': 'HP',
            'model': 'LaserJet Pro M404dn',
            'celNum': '1234567890',
            'description': 'Descripción de la orden de trabajo 1',
            'status': 'Pendiente',
            'created_at': '2023-10-01',
            'assigned_to': 'Usuario 1'
        }
    }
    return render(request, 'detalle_odt.html', context)

def editar_odt(request, odt_id):
    context = {
        'odt': {
            'id': odt_id,
            'typeMachine': 'Impresora',
            'clientName': 'Christopher Muñoz',
            'brand': 'HP',
            'model': 'LaserJet Pro M404dn',
            'celNum': '1234567890',
            'description': 'Descripción de la orden de trabajo 1',
            'status': 'Pendiente',
            'created_at': '2023-10-01',
            'assigned_to': 'Usuario 1'
        }
    }
    return render(request, 'editar_odt.html', context)

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