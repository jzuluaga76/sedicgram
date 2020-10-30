from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    website = models.URLField(max_length=200, blank=True)
    biography = models.TextField(blank=True)
    Phone_number = models.CharField(max_length=20, blank=True)
    profile_picture = models.ImageField(
      upload_to='Users/picture',
      blank=True,
      null=True
    )

<<<<<<< HEAD
    
=======
    prueba = models.CharField(max_legth=100, blank=True)   
>>>>>>> b8731acc99a1c019cc0685631a58f838691d4c82
    create = models.DateTimeField(auto_now_add = True)
    modify = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.user.username