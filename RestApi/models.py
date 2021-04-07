from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator

from django.db import models


class User(AbstractUser):
    Address=models.TextField(blank=True,null=True)
    PhoneNumber = models.CharField(max_length=15, blank=True,verbose_name='PhoneNumber')
    cdNumber = models.CharField(max_length=16, blank=True,verbose_name='cdNumber')
    cdDate=models.DateField(blank=True,null=True,verbose_name='cdDate')
    cdName = models.CharField(max_length=16, blank=True,verbose_name='cdName')
    def __str__(self):
        return self.first_name+" "+self.last_name
class Payments(models.Model):
    method  = models.CharField(blank=False, null=False,max_length=16)
    type  = models.CharField(blank=False, null=False,max_length=16)
    amount  = models.CharField(max_length=4,blank=False, null=False)
    expired_date = models.DateField(blank=False, null=False)
    payment_date   = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        ordering = ('payment_date','user')
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} in {self.payment_date}'

class Actors(models.Model):
    name=models.CharField(blank=False,null=False,max_length=20, unique = True)
    def __str__(self):
        return self.name

class Categories(models.Model):
    name=models.CharField(blank=False,null=False,max_length=20, unique = True)
    def __str__(self):
        return self.name

class Shows(models.Model):
    name = models.CharField(blank=False, null=False, max_length=255)
    maturity_rating  = models.CharField(blank=False, null=False, max_length=3)
    Language = models.CharField(blank=False, null=False, max_length=16)
    Country =models.CharField(blank=False, null=False, max_length=16)
    poster=models.URLField(blank=False,null=False)
    bigPoster=models.URLField(blank=True,null=True)
    trailer = models.URLField(blank=True, null=True)
    likes = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0)])
    disLikes= models.PositiveIntegerField(default=0,validators=[MinValueValidator(0)])
    publishDate=models.DateField(blank=True,null=True)
    views=models.PositiveIntegerField(default=0,validators=[MinValueValidator(0)])
    Description=models.TextField(blank=True,null=True)
    Actors=models.ManyToManyField(Actors)
    Categories=models.ManyToManyField(Categories)

    class Meta:
        ordering     = (['publishDate',])
    def __str__(self):
        return self.name

class Episode(models.Model):
    show = models.ForeignKey(Shows,on_delete=models.CASCADE)
    season = models.IntegerField(null=True,blank=True)
    episode = models.IntegerField(null=True, blank=True)
    name=models.CharField(null=True,blank=True,max_length=50)
    duration=models.IntegerField(null=True,blank=True)
    link=models.URLField(blank=False,null=False)
    date=models.fields.DateField(blank=True,null=True)
    class Meta:
        unique_together = (("show", "season","episode"),)
        ordering = (['date', ])
    def __str__(self):
        if  self.season:
            return f"{self.show.name}  S:{str(self.season)}   E: {str(self.episode)}"
        else:
            return self.show.name
class History(models.Model):
    show =models.ForeignKey(Shows,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
