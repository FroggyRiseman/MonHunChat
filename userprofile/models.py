from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # rank =models.ImageField(choices             -- must do more research and find the icons online
    user = models.OneToOneField(User)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
    return self.user.username
