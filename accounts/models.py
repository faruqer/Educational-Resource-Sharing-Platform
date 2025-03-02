from django.conf import settings
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    institution = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"Profile({self.user.username})"
