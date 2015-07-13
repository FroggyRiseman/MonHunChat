from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

class UserProfile(models.Model):
    LOW_RANK = 'LR'
    HIGH_RANK = 'HR'
    G_RANK = 'GR'
    G_RANK_PLUS = 'GRP'
    GUILD_MASTER = 'GM'

    ranks = (
            (LOW_RANK, 'Low Rank'),
            (HIGH_RANK, 'High Rank'),
            (G_RANK, 'G-Rank'),
            (G_RANK_PLUS, 'G-Rank 100-998'),
            (GUILD_MASTER, 'G-Rank 999'),
    )

    user = models.OneToOneField(User)
    description = models.TextField(max_length=200, null=True, blank=True)
    rank = models.CharField(
            max_length=3,
            choices=ranks,
            default=LOW_RANK,
    )

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        profile, new = UserProfile.objects.get_or_create(user=instance)
