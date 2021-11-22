from django.db import models

from users.models import Artist

class Collaboration(models.Model):
    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE
    )

    hit = models.ForeignKey(
        'hits.Hit',
        on_delete=models.CASCADE
    )

    message = models.TextField(
        blank=True
    )

    song = models.FileField(
        upload_to="hits/collaborations/",
        blank=True
    )

    created = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.artist} colab on {self.created}"
