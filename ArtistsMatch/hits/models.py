"""Hit model module"""
from django.db import models
from users.models import Artist


class Hit(models.Model):
    """Hit model"""

    title = models.CharField(
        max_length=200,
        blank=False
    )
    description = models.TextField(
        blank=True
    )
    song = models.FileField(
        upload_to='hits/songs',
        blank=False
    )
    cover = models.FileField(
        upload_to='hits/covers',
        blank=False    
    )

    colaborators = models.ManyToManyField(
        to=Artist
    )