from django.db import models

class Apoderado(models.Model):
    apoderado_id = models.AutoField(primary_key=True)
    apoderado_nombre = models.CharField(max_length=255)
    apoderado_apellido = models.CharField(max_length=255)
    apoderado_telefono = models.CharField(max_length=255)
    apoderado_documento_identidad = models.CharField(max_length=20)

