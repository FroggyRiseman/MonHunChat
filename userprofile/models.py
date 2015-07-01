from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.TextField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    # rank = models.ImageField(choices             -- must do more research and find the icons online

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)
