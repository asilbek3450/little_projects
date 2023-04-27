from django.contrib import admin

from myfiles.models import *


# Register your models here.
class Cityv(admin.ModelAdmin):
    list_display = ['id','manzil']

admin.site.register(Citys,Cityv)

class viloyat(admin.ModelAdmin):
    list_display = ['id','viloyat']

admin.site.register(Viloyatlar,viloyat)