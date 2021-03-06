from django.db import models
from django.contrib.auth.models import User


def nameFile(instance, filename):
    return '/'.join(['images', str(instance.user.username), filename])


class UserSetting(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=nameFile, blank=True, null=True)
    about = models.TextField()
    theme_type = models.CharField(max_length=32)
    theme_name = models.CharField(max_length=32)

    def __str__(self):
        return self.user.username + " setting"
