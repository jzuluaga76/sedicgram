from django.db import models
from django.contrib.auth.models import User
from Users.models import Profile
from Post import picture

# Create your models here.

class Post(models.Model):
 user = models.ForeignKey(User, on_delete= models.CASCADE)
 profile = models.ForeignKey(Profile, on_delete= models.CASCADE)
 title = models.CharField(max_length=20, blank=True)
 photo = models.ImageField(
      upload_to='Post/picture',
      blank=True,
      null=True
 )
 postdate = models.DateTimeField(auto_now_add = True)
 modify = models.DateTimeField(auto_now = True)

 def __str__(self):
        return '{} by @{}'.format(self.title, self.user.username)