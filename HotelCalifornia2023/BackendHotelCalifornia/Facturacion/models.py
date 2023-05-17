from django.db import models
from myapp.models import Hotel, Cliente, Reserva

class Factura(models.Model):
    facturaId = models.AutoField(primary_key=True)
    nroFactura = models.TextField(max_length=10, blank=False)
    hotelId = models.ForeignKey(Hotel, to_field="hotelId", on_delete=models.CASCADE)
    clienteId = models.ForeignKey(Cliente, to_field="clienteId", on_delete=models.CASCADE)
    class Meta:
        db_table = "factura"
        verbose_name = "Facturas emitidas por el hotel correspondientes a las resvervas"
        verbose_name_plural = "Facturas"
    def __unicode__(self):
        return "Factura"
    def __str__(self) -> str:
        return f"Factura Nº {self.nroFactura}"
    
class Detalle(models.Model):
    detalleId = models.AutoField(primary_key=True)
    facturaId = models.ForeignKey(Factura, to_field="facturaId", on_delete=models.CASCADE)
    reservaId = models.ForeignKey(Reserva, to_field="reservaId", on_delete=models.CASCADE)
    descuento = models.DecimalField(max_digits=4, decimal_places=2, default=0, blank=False)
    importe = models.DecimalField(max_digits=20, decimal_places=2, default=0, blank=False)
    class Meta:
        db_table = "detalle"
        verbose_name = "Detalle de las facturas emitidas por el hotel correspondientes a las resvervas"
        verbose_name_plural = "Detalles"
    def __unicode__(self):
        return "Detalle"
    def __str__(self) -> str:
        return f"El detalle corresponde a la reserva {self.reservaId} con un importe total de $ {self.importe}"
    
class TipoPago(models.Model):
    tipoPagoId = models.AutoField(primary_key=True)
    tipoPago = models.CharField(max_length=30, blank=False)
    class Meta:
        db_table = "tipoPagp"
        verbose_name = "Tipo de Pago de las facturas"
        verbose_name_plural = "Tipos de pago"
    def __unicode__(self):
        return self.tipo
    def __str__(self) -> str:
        return self.tipo
    
class DetallePago(models.Model):
    detallePagoId = models.AutoField(primary_key=True)
    facturaId = models.ForeignKey(Factura, to_field="facturaId", on_delete=models.CASCADE)
    tipoPagoId = models.ForeignKey(TipoPago, to_field="tipoPagoId", on_delete=models.CASCADE)
    porcentajePago = models.PositiveSmallIntegerField(max_length=3)
    class Meta:
        db_table = "detallePagp"
        verbose_name = "Detalle de Pago de las facturas emitidas por el hotel"
        verbose_name_plural = "Detalles de pago"
    def __unicode__(self):
        return "DetallePago"
    def __str__(self) -> str:
        return f"El detalle de pago correspondiente a la factura {self.facturaId}"
    
