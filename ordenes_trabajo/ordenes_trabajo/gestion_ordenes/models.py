from django.db import models

# Create your models here.
class OrdenTrabajo(models.Model):
    odtId = models.AutoField(primary_key=True)
    odtFecha = models.DateTimeField(auto_now_add=True)
    odtDescripcion = models.TextField()
    odtEstado = models.CharField(max_length=20, default='Pendiente')
    odtModelo = models.CharField(max_length=50)
    odtMarca = models.CharField(max_length=50)
    odtFalla = models.TextField(blank=True, null=True)
    odtCreadoPor = models.CharField(max_length=50, blank=True, null=True)
    odtAsignadoA = models.CharField(max_length=50, blank=True, null=True)
    odtFechaEntrega = models.DateTimeField(blank=True, null=True)


class datosCliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    clienteNombre = models.CharField(max_length=100)
    clienteTelefono = models.CharField(max_length=15)
    clienteEmail = models.EmailField(blank=True, null=True)
    clienteDireccion = models.CharField(max_length=255, blank=True, null=True)
    clienteOdtId = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='clientes')

class pago(models.Model):
    pagoId = models.AutoField(primary_key=True)
    pagoFecha = models.DateTimeField(auto_now_add=True)
    pagoMonto = models.DecimalField(max_digits=10, decimal_places=2)
    pagoMetodo = models.CharField(max_length=20, choices=[
        ('Efectivo', 'Efectivo'),
        ('Tarjeta', 'Tarjeta'),
        ('Transferencia', 'Transferencia'),
    ])
    pagoOdtId = models.ForeignKey(OrdenTrabajo, on_delete=models.CASCADE, related_name='pagos')