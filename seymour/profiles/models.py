from django.db import models
from django.contrib.auth.models import User

from registration.signals import user_registered

# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, unique=True, related_name="profile")
	mark_read_after = models.IntegerField(default=7)


def createProfile(sender, instance, **kwargs):
    user_profile = Profile.objects.create(user=instance)

user_registered.connect(createProfile, sender=User)