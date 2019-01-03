from django.db import models


class S(models.Model):
    xh = models.CharField(max_length=200)
    xm = models.CharField(max_length=200)
    xb = models.CharField(max_length=200)
    csrq = models.DateField(null=True)
    jg = models.CharField(max_length=200)
    sjhm = models.CharField(max_length=200)
    yxh = models.CharField(max_length=200)


class C(models.Model):
    kh = models.CharField(max_length=200)
    km = models.CharField(max_length=200)
    xf = models.IntegerField(null=True)
    xs = models.IntegerField(null=True)
    yxh = models.CharField(max_length=200)


class D(models.Model):
    yxh = models.CharField(max_length=200)
    mc = models.CharField(max_length=200)
    dz = models.CharField(max_length=200)
    lxdh = models.CharField(max_length=200)


class E(models.Model):
    xh = models.CharField(max_length=200)
    xq = models.CharField(max_length=200)
    kh = models.CharField(max_length=200)
    gh = models.CharField(max_length=200)
    pscj = models.IntegerField(null=True)
    kscj = models.IntegerField(null=True)
    zpcj = models.IntegerField(null=True)


class O(models.Model):
    xq = models.CharField(max_length=200)
    kh = models.CharField(max_length=200)
    gh = models.CharField(max_length=200)
    sksj = models.CharField(max_length=200)


class T(models.Model):
    gh = models.CharField(max_length=200)
    xm = models.CharField(max_length=200)
    xb = models.CharField(max_length=200)
    csrq = models.DateField(null=True)
    xl = models.CharField(max_length=200)
    jbgz = models.FloatField(null=True)
    yxh = models.CharField(max_length=200)
