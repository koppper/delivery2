from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/profile/")
    instagram = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
