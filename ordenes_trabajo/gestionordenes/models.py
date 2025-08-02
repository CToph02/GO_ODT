from django.db import models
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
    odtId = models.AutoField(primary_key=True)
    # Datos Cliente
    odtClientName = models.CharField(max_length=100, null=True)
    odtClientPhone = models.CharField(max_length=15, null=True)
    odtClientEmail = models.EmailField(blank=True, null=True)
    odtClientAddress = models.CharField(max_length=255, blank=True, null=True)
    # Datos ODT
    odtNumero = models.CharField(max_length=20, unique=True)
    odtFecha = models.DateTimeField(auto_now_add=True, null=True)
    odtDescripcion = models.TextField(null=True)
    odtEstado = models.CharField(max_length=20, default='Pendiente', null=True)
    odtModelo = models.CharField(max_length=50, null=True)
    odtMarca = models.CharField(max_length=50, null=True)
    odtFalla = models.TextField(blank=True, null=True)
    odtTipoMaquina = models.CharField(max_length=50, null=True)
    # Datos pago
    odtDiagnostico = models.TextField(blank=True, null=True)
    odtPaymentForm = models.CharField(max_length=20, null=True)
    
    def __str__(self):
        return f"ODT {self.odtNumero}"
    
    class Meta:
        verbose_name = 'Orden de Trabajo'
        verbose_name_plural = 'Órdenes de Trabajo'
        ordering = ['-odtFecha']
        db_table = 'orden_trabajo'

class Pago(models.Model):
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