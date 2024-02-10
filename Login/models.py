from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True, verbose_name='用户ID')
    job_number = models.CharField(max_length=50, verbose_name='job number', null=True)
    username = models.CharField(max_length=50, verbose_name='username')
    password = models.CharField(max_length=50, verbose_name='password')
    role = models.IntegerField(verbose_name='role', choices=((1, 'admin'), (2, 'stuff')))

class Work(models.Model):
    job_number = models.CharField(max_length=50, verbose_name='job number')
    checkin_time = models.DateTimeField(verbose_name='check in time')
    checkout_time = models.DateTimeField(verbose_name='check out time', null=True)

