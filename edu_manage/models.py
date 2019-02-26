from django.db import models


class S(models.Model):
    id = models.AutoField(primary_key=True)
    xh = models.CharField(max_length=200)
    xm = models.CharField(max_length=200)
    xb = models.CharField(max_length=200)
    csrq = models.DateField(null=True)
    jg = models.CharField(max_length=200)
    sjhm = models.CharField(max_length=200)
    yxh = models.CharField(max_length=200)
    psw = models.CharField(max_length=200)


class C(models.Model):
    id = models.AutoField(primary_key=True)
    kh = models.CharField(max_length=200)
    km = models.CharField(max_length=200)
    xf = models.IntegerField(null=True)
    xs = models.IntegerField(null=True)
    yxh = models.CharField(max_length=200)


class D(models.Model):
    id = models.AutoField(primary_key=True)
    yxh = models.CharField(max_length=200)
    mc = models.CharField(max_length=200)
    dz = models.CharField(max_length=200)
    lxdh = models.CharField(max_length=200)


class E(models.Model):
    id = models.AutoField(primary_key=True)
    xh = models.CharField(max_length=200)
    xq = models.CharField(max_length=200)
    kh = models.CharField(max_length=200)
    gh = models.CharField(max_length=200)
    pscj = models.IntegerField(null=True)
    kscj = models.IntegerField(null=True)
    zpcj = models.IntegerField(null=True)
    # 与课程名建立一对多的关系
    course = models.ForeignKey(to='C', to_field='id', on_delete=models.CASCADE, default=None)
    # 与教师建立一对多的关系
    teacher = models.ForeignKey(to='T', to_field='id', on_delete=models.CASCADE, default=None)


class O(models.Model):
    id = models.AutoField(primary_key=True)
    # 与课程名建立一对多的关系
    course = models.ForeignKey(to='C', to_field='id', on_delete=models.CASCADE, default=None)
    # 与教师建立一对多的关系
    teacher = models.ForeignKey(to='T', to_field='id', on_delete=models.CASCADE, default=None)
    xq = models.CharField(max_length=200)
    kh = models.CharField(max_length=200)
    gh = models.CharField(max_length=200)
    sksj = models.CharField(max_length=200)


class T(models.Model):
    id = models.AutoField(primary_key=True)
    gh = models.CharField(max_length=200)
    xm = models.CharField(max_length=200)
    xb = models.CharField(max_length=200)
    csrq = models.DateField(null=True)
    xl = models.CharField(max_length=200)
    jbgz = models.FloatField(null=True)
    yxh = models.CharField(max_length=200)
    psw = models.CharField(max_length=200)
