from django.db import models

class Mimodelo(models.Model):
    campo_1 = models.CharField(max_length=100)
    campo_2 = models.ImageField()
    campo_3 = models.DateTimeField()
