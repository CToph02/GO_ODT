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

class OrdenTrabajo(models.Model):
    odtId = models.AutoField(primary_key=True)
    # Datos Cliente
    odtClientName = models.CharField(max_length=100, null=True)
    odtClientPhone = models.CharField(max_length=15, null=True)
    odtClientEmail = models.EmailField(blank=True, null=True)
    odtClientAddress = models.CharField(max_length=255, blank=True, null=True)
    # Datos ODT
    odtNumero = models.CharField(max_length=20, unique=True, blank=True)
    odtFecha = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    #odtDescripcion = models.TextField(null=True)
    odtEstado = models.CharField(max_length=20, default='Pendiente', null=True)
    odtModelo = models.CharField(max_length=50, null=True)
    odtMarca = models.CharField(max_length=50, null=True)
    odtFalla = models.TextField(blank=True, null=True)
    odtTipoMaquina = models.CharField(max_length=50, null=True)
    odtRecepcion = models.CharField(max_length=50, null=True, blank=True)
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

    def save(self, *args, **kwargs):
        if not self.odtNumero:
            ultimo = OrdenTrabajo.objects.order_by('-odtId').first()
            if ultimo and ultimo.odtNumero.startswith('ODT-'):
                ultimo_num = int(ultimo.odtNumero.split('-')[1])
                nuevo_num = ultimo_num + 1
            else:
                nuevo_num = 1
            self.odtNumero = f'ODT-{nuevo_num:06d}'
        super().save(*args, **kwargs)

class Tecnicos(models.Model):
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

class Estado(models.Model):
    estadoId = models.AutoField(primary_key=True)
    estadoNombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.estadoNombre
    
    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        ordering = ['estadoNombre']
        db_table = 'estado'

class TipoMaquina(models.Model):
    tipoId = models.AutoField(primary_key=True)
    tipoNombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.tipoNombre
    
    class Meta:
        verbose_name = 'Tipo de Máquina'
        verbose_name_plural = 'Tipos de Máquina'
        ordering = ['tipoNombre']
        db_table = 'tipo_maquina'

class Impresora(models.Model):
    impresoraId = models.AutoField(primary_key=True)
    impresoraNombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.impresoraNombre
    
    class Meta:
        verbose_name = 'Impresora'
        verbose_name_plural = 'Impresoras'
        ordering = ['impresoraNombre']
        db_table = 'impresora'

class Modelo(models.Model):
    modeloId = models.AutoField(primary_key=True)
    modeloNombre = models.CharField(max_length=50)
    impresora_id = models.ForeignKey(Impresora, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.modeloNombre
    
    class Meta:
        verbose_name = 'Modelo'
        verbose_name_plural = 'Modelos'
        ordering = ['modeloNombre']
        db_table = 'modelo'