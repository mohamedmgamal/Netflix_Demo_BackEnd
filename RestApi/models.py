from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):
    Address=models.TextField(blank=True,null=True)
    PhoneNumber = models.CharField(max_length=15, blank=True,verbose_name='PhoneNumber')
    cdNumber = models.CharField(max_length=16, blank=True,verbose_name='cdNumber')
    cdDate=models.DateField(blank=True,null=True,verbose_name='cdDate')
    cdName = models.CharField(max_length=16, blank=True,verbose_name='cdName')
    def __str__(self):
        return self.first_name+" "+self.last_name
