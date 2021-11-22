"""Hits admin module"""
from django.contrib import admin

from hits.models import Collaboration, Hit

admin.site.register(Hit)
admin.site.register(Collaboration)