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
            },
            {
                'id': 4,
                'typeMachine': 'Escáner',
                'brand': 'Epson',
                'model': 'Perfection V600',
                'clientName': 'María López',
                'celNum': '5566778899',
                'description': 'Descripción de la orden de trabajo 4',
                'status': 'Pendiente',
                'created_at': '2023-10-04',
                'assigned_to': 'Usuario 4'
            },
            {
                'id': 5,
                'typeMachine': 'Fotocopiadora',
                'brand': 'Xerox',
                'model': 'WorkCentre 6515',
                'clientName': 'Carlos Fernández',
                'celNum': '2233445566',
                'description': 'Descripción de la orden de trabajo 5',
                'status': 'En Proceso',
                'created_at': '2023-10-05',
                'assigned_to': 'Usuario 5'
            },
            {
                'id': 6,
                'typeMachine': 'Impresora',
                'brand': 'Lexmark',
                'model': 'MB2236adw',
                'clientName': 'Sofía Martínez',
                'celNum': '3344556677',
                'description': 'Descripción de la orden de trabajo 6',
                'status': 'Completada',
                'created_at': '2023-10-06',
                'assigned_to': 'Usuario 6'
            },
            {
                'id': 7,
                'typeMachine': 'Plotter',
                'brand': 'HP',
                'model': 'DesignJet T120',
                'clientName': 'Javier Torres',
                'celNum': '4455667788',
                'description': 'Descripción de la orden de trabajo 7',
                'status': 'Pendiente',
                'created_at': '2023-10-07',
                'assigned_to': 'Usuario 7'
            },
            {
                'id': 8,
                'typeMachine': 'Escáner',
                'brand': 'Canon',
                'model': 'CanoScan LiDE 400',
                'clientName': 'Laura Ramírez',
                'celNum': '5566778899',
                'description': 'Descripción de la orden de trabajo 8',
                'status': 'En Proceso',
                'created_at': '2023-10-08',
                'assigned_to': 'Usuario 8'
            },
            {
                'id': 9,
                'typeMachine': 'Escáner',
                'brand': 'Canon',
                'model': 'CanoScan LiDE 400',
                'clientName': 'Laura Ramírez',
                'celNum': '5566778899',
                'description': 'Descripción de la orden de trabajo 8',
                'status': 'En Proceso',
                'created_at': '2023-10-08',
                'assigned_to': 'Usuario 8'
            },
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

def estado(request):
    context = {
        'odt_id': "odt_id",
        'status': 'Pendiente'  # Example status
    }
    return render(request, 'estado.html', context)