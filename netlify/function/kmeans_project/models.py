from django.db import models

# Create your models here.

class Input(models.Model):
    data1 = models.CharField(max_length=100)
    data2 = models.CharField(max_length=100)
    k = models.CharField(max_length=100)
    # tambahkan bidang lain yang Anda perlukan untuk logika Anda
