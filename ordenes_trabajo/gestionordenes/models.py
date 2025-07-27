from django.db import models
#from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    clienteNombre = models.CharField(max_length=100)
    clienteTelefono = models.CharField(max_length=15)
    clienteEmail = models.EmailField(blank=True, null=True)
    clienteDireccion = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.clienteNombre
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['clienteNombre']
        db_table = 'cliente'

class EstadoOrden(models.Model):
    estadoId = models.AutoField(primary_key=True)
    estadoNombre = models.CharField(max_length=50)
    estadoDescripcion = models.TextField(blank=True, null=True)
    estadoColor = models.CharField(max_length=7, choices=[
        ('#FF0000', 'Sin reparación'),
        ('#00FF00', 'Lista'),
        ('#0000FF', 'Diagnosticada'),
        ('#FFA500', 'No repara'),
        ('#FFFF00', 'En reparación'),
    ], default='#FFFFFF')
    
    def __str__(self):
        return self.estadoNombre
    
    class Meta:
        verbose_name = 'Estado de Orden'
        verbose_name_plural = 'Estados de Órdenes'
        ordering = ['estadoNombre']
        db_table = 'estado_orden'

class OrdenTrabajo(models.Model):
    # Datos ODT
    odtId = models.AutoField(primary_key=True)
    odtNumero = models.CharField(max_length=20, unique=True)
    odtFecha = models.DateTimeField(auto_now_add=True, null=True)
    odtDescripcion = models.TextField(null=True)
    odtEstado = models.CharField(max_length=20, default='Pendiente', null=True)
    odtModelo = models.CharField(max_length=50, null=True)
    odtMarca = models.CharField(max_length=50, null=True)
    odtFalla = models.TextField(blank=True, null=True)
    odtTipoMaquina = models.CharField(max_length=50, choices=[
        ('impresora', 'Impresora'),
        ('plotter', 'Plotter'),
        ('otro', 'Otro'),
    ], default='impresora')

    # cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    # creadoPor = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    # asignadoA = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='ordenes_asignadas')
    # estadoOrden = models.ForeignKey(EstadoOrden, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return f"ODT {self.odtNumero}"# - {self.cliente.clienteNombre}"
    
    class Meta:
        verbose_name = 'Orden de Trabajo'
        verbose_name_plural = 'Órdenes de Trabajo'
        ordering = ['-odtFecha']  # Más recientes primero
        db_table = 'orden_trabajo'

class Pago(models.Model):  # Cambié el nombre a PascalCase
    pagoId = models.AutoField(primary_key=True)
    pagoFecha = models.DateTimeField(auto_now_add=True)
    pagoMonto = models.DecimalField(max_digits=10, decimal_places=2)
    pagoMetodo = models.CharField(max_length=20, choices=[
        ('efectivo', 'Efectivo'),
        ('debito', 'Tarjeta de débito'),
        ('credito', 'Tarjeta de crédito'),
        ('transferencia', 'Transferencia'),
    ])
    ordenTrabajo = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='pagos')
    
    def __str__(self):
        return f"Pago ${self.pagoMonto} - ODT {self.ordenTrabajo.odtNumero}"
    
    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['-pagoFecha']
        db_table = 'pago'

class Tecnico(models.Model):
    tecnicoId = models.AutoField(primary_key=True)
    tecnicoNombre = models.CharField(max_length=100)
    tecnicoTelefono = models.CharField(max_length=15)
    tecnicoEmail = models.EmailField(blank=True, null=True)
    
    def __str__(self):
        return self.tecnicoNombre
    
    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        ordering = ['tecnicoNombre']
        db_table = 'tecnico'