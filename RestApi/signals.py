from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import User
@receiver(post_save,sender=User)
def Handler(sender,instance,created,*args,**kwargs):
    if created:
        print("email sent to :",instance.email)
        send_mail("Welcome to Netflix",f'welcome {instance.first_name} {instance.last_name} to netflix ',"netflixdemoiti@gmail.com",[instance.email,],fail_silently=True)