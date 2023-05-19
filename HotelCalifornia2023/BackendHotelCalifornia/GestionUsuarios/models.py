from django.db import models

class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    correo = models.CharField(max_length=100, blank=False)
    contraseña = models.CharField(max_length=150, blank=False)
    fechadenacimiento = models.DateField(blank=False)
    class Meta:
        db_table = "Cliente"
        verbose_name = "Todos los clientes registrados en el Hotel"
        verbose_name_plural = "Clientes"
        def __unicode__(self):
            return "Cliente"
        def __str__(self):
            return self.nombre