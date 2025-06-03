from django.contrib import admin

# Register your models here.

from .models import Producto, Remito

admin.site.register(Producto, Remito)


