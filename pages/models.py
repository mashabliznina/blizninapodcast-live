from django.db import models
from django.db.models.base import Model
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse
from tinymce.models import HTMLField


class Comment(models.Model):
    episode = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    name = models.TextField(max_length=20)
    text = models.TextField()

    def get_absolute_url(self):
        return reverse('episode_detail', args=[str(self.id)])

    

    def __str__(self):
        return self.name[:50]


class Episode(models.Model):
    theme = models.CharField(max_length=50)
    date = models.DateTimeField(null=True)
    title = models.CharField(max_length=150, null=True)
    body = HTMLField()
    preview = models.CharField(max_length=100, null=True)
    buzz_id = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.title[:50]
