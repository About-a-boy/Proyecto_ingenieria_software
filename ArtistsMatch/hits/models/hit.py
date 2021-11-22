"""Hit model module"""
from django.db import models
# from django.utils import timezone

from users.models import Artist
from hits.models import Collaboration

class Hit(models.Model):
    """Hit model"""

    title = models.CharField(
        max_length=200,
        blank=True
    )
    description = models.TextField(
        blank=True
    )
    song = models.FileField(
        upload_to='hits/songs',
        blank=True
    )
    cover = models.FileField(
        upload_to='hits/covers',
        blank=True,
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    collaborators = models.ManyToManyField(
        Artist,
        through=Collaboration,
        through_fields=("hit", "artist")
    )

    def __str__(self):
        return f"{self.title}"
