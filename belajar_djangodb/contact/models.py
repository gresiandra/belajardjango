from django.db import models

# Create your models here.

class contactModel(models.Model):
    nama = models.CharField(max_length=20)
    jenis_kelamin = models.CharField(max_length=1)
    email = models.EmailField()
    alamat = models.TextField()

    def __str__(self):
        return '{}. {}'.format(self.id, self.nama)