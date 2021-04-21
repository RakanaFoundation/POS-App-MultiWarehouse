# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Jabatan(models.Model):
    jabatan = models.CharField(max_length=125)

    def __str__(self):
        return self.jabatan

class Distrik(models.Model):
    nama_distrik = models.CharField(max_length=125)

    def __str__(self):
        return self.nama_distrik

class Toko(models.Model):
    nama_toko = models.CharField(max_length=30)
    distrik_id = models.ForeignKey(Distrik, on_delete=models.CASCADE)
    alamat = models.CharField(max_length=250)

    def __str__(self):
        return self.nama_toko

class Employee(models.Model):
    nama_toko = models.ForeignKey(Toko, on_delete=models.CASCADE)
    nik = models.CharField(max_length=20)
    nip = models.CharField(max_length=20)
    nama_pegawai = models.CharField(max_length=225)
    tgl_masuk = models.DateField()
    tempat_lahir = models.CharField(max_length=50)
    tgl_lahir = models.DateField()
    jabatan = models.ForeignKey(Jabatan, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nama_pegawai

class Dept_Grup(models.Model):
    kode_dept_grup = models.CharField(max_length=5)
    nama_dept_grup = models.CharField(max_length=50)

    def __str__(self):
        return '%s %s' % (self.kode_dept_grup, self.nama_dept_grup)

class Dept(models.Model):
    kode_dept = models.CharField(max_length=5)
    nama_dept = models.CharField(max_length=125)
    kode_dept_grup = models.ForeignKey(Dept_Grup, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.kode_dept, self.nama_dept)

class MClass(models.Model):
    kode_mclass = models.CharField(max_length=4)
    nama_mclass = models.CharField(max_length=225)
    kode_dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.kode_mclass, self.nama_mclass)

class Supplier(models.Model):
    nama_supplier = models.CharField(max_length=125)
    aktif = models.BooleanField(default=False)

    def __str__(self):
        return self.nama_supplier

class Buyer(models.Model):
    nama_buyer = models.CharField(max_length=125)
    aktif = models.BooleanField(default=False)

    def __str__(self):
        return self.nama_buyer

class Merk(models.Model):
    kode_merk = models.CharField(max_length=4)
    merk = models.CharField(max_length=50)
    kode_mclass = models.ForeignKey(MClass, on_delete=models.CASCADE)
    kode_supp = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    nama_buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    margin = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.kode_merk, self.merk)

class Measurement(models.Model):
    unit = models.CharField(max_length=10)
    konversi = models.IntegerField()

    def __str__(self):
        return self.unit

class Size(models.Model):
    size = models.CharField(max_length=20)

    def __str__(self):
        return self.size

class SKU(models.Model):
    sku = models.BigIntegerField()
    barcode = models.BigIntegerField()
    sku_desc = models.CharField(max_length=225)
    harga_jual = models.IntegerField()
    harga_beli = models.IntegerField()
    harga_beli_besar = models.BigIntegerField()
    hpp = models.IntegerField()
    stock = models.IntegerField()
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)
    mclass = models.ForeignKey(MClass, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    merk = models.ForeignKey(Merk, on_delete=models.CASCADE)
    article = models.CharField(max_length=50)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    sku_aktif = models.BooleanField()
    sku_flag = models.BooleanField()
    diskon = models.IntegerField()
    mulai_diskon = models.DateField()
    akhir_diskon = models.DateField()


    def __str__(self):
        return self.sku_desc