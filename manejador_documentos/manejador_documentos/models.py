from django.db import models

class Documento(models.Model):
    Id = models.AutoField(primary_key=True)
    identificacion = models.IntegerField()
    tipo = models.CharField(max_length=50)
    ruta = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.Id)