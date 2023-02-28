from django.db import models

# Create your models here.
class Viloyatlar(models.Model):
    viloyat = models.CharField(max_length=50)
    def __str__(self):
        return self.viloyat
    class Meta:
        verbose_name ="Viloyatlar"
        verbose_name_plural ="Viloyatlar"
        
        
class Citys(models.Model):
    manzil = models.ForeignKey(Viloyatlar,on_delete=models.CASCADE,)
    class Meta:
        verbose_name ="Shaharlar"
        verbose_name_plural ="Shaharlar"
        