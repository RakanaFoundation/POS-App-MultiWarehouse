# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from app.models import Distrik, Jabatan, Toko, Employee, Dept_Grup, Dept, MClass, Supplier, Buyer, Merk, Measurement, Size, SKU

# Register your models here.
admin.site.register(Distrik)
admin.site.register(Jabatan)
admin.site.register(Toko)
admin.site.register(Employee)
admin.site.register(Dept_Grup)
admin.site.register(Dept)
admin.site.register(MClass)
admin.site.register(Supplier)
admin.site.register(Buyer)
admin.site.register(Merk)
admin.site.register(Measurement)
admin.site.register(Size)
admin.site.register(SKU)