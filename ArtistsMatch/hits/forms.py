"""Hits forms module"""
from django import forms

from hits.models import Hit

class CreateHitForm(forms.ModelForm):
    """Create Hit Form"""

    class Meta:
        model = Hit
        fields = [ 'title', 'description', 'song', 'cover' ]