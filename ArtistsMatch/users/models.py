"""Users models"""
from django.contrib.auth.models import User
from django.db import models


class Artist(models.Model):
    """Artist model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    photo = models.ImageField(
        upload_to="users/pictures",
        blank=True,
        null=True,
    )
    artist_name = models.CharField(
        max_length=100,
        blank=False,
        unique=True,
    )
    fullname = models.CharField(
        max_length=500,
        blank=False
    )
    email = models.EmailField(
        blank=True,
        unique=True
    )
    bio = models.TextField(
        blank=True
    )

    def __str__(self):
        """Return username"""
        return f"Artist {self.user.username}"
