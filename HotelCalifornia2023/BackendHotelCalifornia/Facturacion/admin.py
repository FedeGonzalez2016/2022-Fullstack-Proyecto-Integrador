from django.contrib import admin
from .models import Factura, Detalle, DetallePago, TipoPago

class FacturaAdmin(admin.ModelAdmin):
    list_display = ("nroFactura", "hotelId", "clienteId")
class DetalleAdmin(admin.ModelAdmin):
    list_display = ("facturaId", "reservaId", "descuento", "importe")
class DetallePagoAdmin(admin.ModelAdmin):
    list_display = ("facturaId", "tipoPagoId", "porcentajePago")
class TipoPagoAdmin(admin.ModelAdmin):
    list_display = ("tipoPago")

admin.site.register(Factura, FacturaAdmin)
admin.site.register(Detalle, DetalleAdmin)
admin.site.register(DetallePago, DetallePagoAdmin)
admin.site.register(TipoPago, TipoPagoAdmin)