from django.contrib import admin
from django.db import models
from tinymce.widgets import TinyMCE

from .models import Comment, Episode

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ["title"]
    formfield_overrides = {
        models.TextField: { 'widget': TinyMCE() }
    }

admin.site.register(Comment)
admin.site.register(Episode, EpisodeAdmin)
