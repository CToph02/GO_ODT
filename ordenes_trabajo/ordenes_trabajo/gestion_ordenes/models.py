from django.db import models

# Create your models here.
class OrdenTrabajo(models.Model):
    # Datos ODT
    odtId = models.AutoField(primary_key=True)
    odtNumero = models.CharField(max_length=20, unique=True)
    odtFecha = models.DateTimeField(auto_now_add=True)
    odtDescripcion = models.TextField()
    odtEstado = models.CharField(max_length=20, default='Pendiente')
    odtModelo = models.CharField(max_length=50)
    odtMarca = models.CharField(max_length=50)
    odtFalla = models.TextField(blank=True, null=True)
    odtFechaEntrega = models.DateTimeField(blank=True, null=True)

    #Relaciones
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    creadoPor = models.ForeignKey('User', blank=True, null=True)
    asignadoA = models.CharField('User', blank=True, null=True)
    estadoOrden = models.ForeignKey('EstadoOrden', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = 'Orden de Trabajo'
        verbose_name_plural = 'Órdenes de Trabajo'
        ordering = ['odtFecha']
        db_table = 'orden_trabajo'

class EstadoOrden(models.Model):
    estadoId = models.AutoField(primary_key=True)
    estadoNombre = models.CharField(max_length=50)
    estadoDescripcion = models.TextField(blank=True, null=True)
    estadoOdtId = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='estados')
    estadoColor = models.CharField(max_length=7, default='#FFFFFF')

    class Meta:
        verbose_name = 'Estado de Orden'
        verbose_name_plural = 'Estados de Órdenes'
        ordering = ['estadoNombre']
        db_table = 'estado_orden'
    
class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    clienteNombre = models.CharField(max_length=100)
    clienteTelefono = models.CharField(max_length=15)
    clienteEmail = models.EmailField(blank=True, null=True)
    clienteDireccion = models.CharField(max_length=255, blank=True, null=True)
    clienteOdtId = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='clientes')

    class Meta:
        verbose_name = 'Datos del Cliente'
        verbose_name_plural = 'Datos de Clientes'
        ordering = ['clienteNombre']
        db_table = 'datos_cliente'

class pago(models.Model):
    pagoId = models.AutoField(primary_key=True)
    pagoFecha = models.DateTimeField(auto_now_add=True)
    pagoMonto = models.DecimalField(max_digits=10, decimal_places=2)
    pagoMetodo = models.CharField(max_length=20, choices=[
        ('Efectivo', 'Efectivo'),
        ('Tarjeta de débito', 'Tarjeta de débito'),
        ('Tarjeta de crédito', 'Tarjeta de crédito'),
        ('Transferencia', 'Transferencia'),
    ])
    pagoOdtId = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='pagos')

    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['pagoFecha']
        db_table = 'pago'