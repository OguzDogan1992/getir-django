from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kategori(models.Model):
    isim = models.CharField(max_length=100)
    resim = models.FileField(upload_to='urunler/', null=True)
    def __str__(self):
        return self.isim
    
class Urun(models.Model):
    isim = models.CharField(max_length=35)
    resim = models.FileField(upload_to='urun/', null=True)
    fiyat = models.IntegerField()
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return self.isim
    
class Sepet(models.Model):
    owner =models.ForeignKey(User, on_delete=models.CASCADE)
    urun = models.ForeignKey(Urun, on_delete=models.CASCADE)
    adet = models.IntegerField()
    toplamFiyat = models.IntegerField()
    odendiMi = models.BooleanField(default=False)

    def __str__(self):
        return self.urun.isim
