from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

class UserProfile(models.Model):
    LOW_RANK_ONE = 'hr1'
    LOW_RANK_TWO = 'hr2'
    LOW_RANK_THREE = 'hr3'
    HIGH_RANK_FOUR = 'hr4'
    HIGH_RANK_FIVE = 'hr5'
    HIGH_RANK_SIX = 'hr6'
    HIGH_RANK_SEVEN = 'hr7'
    G_RANK_EIGHT = 'hr8'
    G_RANK_NINE = 'hr9'

    ranks = (
            (LOW_RANK_ONE, 'HR1'),
            (LOW_RANK_TWO, 'HR2'),
            (LOW_RANK_THREE, 'HR3'),
            (HIGH_RANK_FOUR, 'HR4'),
            (HIGH_RANK_FIVE, 'HR5'),
            (HIGH_RANK_SIX, 'HR6'),
            (HIGH_RANK_SEVEN, 'HR7'),
            (G_RANK_EIGHT, 'HR8'),
            (G_RANK_NINE, 'HR9'),
    )

    user = models.OneToOneField(User)
    description = models.TextField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    rank = models.CharField(
            max_length=3,
            choices=ranks,
            default=LOW_RANK_ONE,
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)
