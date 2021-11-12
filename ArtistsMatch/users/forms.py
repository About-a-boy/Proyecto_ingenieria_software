from django import forms
from django.contrib.auth.models import User

from users.models import Artist

class SignUpForm(forms.Form):
    artist_name = forms.CharField(
        min_length=5,
        max_length=200,
        required=True
    )
    email = forms.CharField(
        widget=forms.EmailInput(),
        required=True
    )
    password = forms.CharField(
        min_length=5,
        required=True,
        widget=forms.PasswordInput()
    )

    def clean_artist_name(self):
        """Ensure if artist name is unique"""
        artist_name = self.cleaned_data["artist_name"]
        artist_name_taken = User.objects.filter(username=artist_name).exists()

        if artist_name_taken:
            raise forms.ValidationError("Ese nombre ya está en uso")
        
        return artist_name
    
    def save(self):
        """save object"""
        data = self.cleaned_data
        
        user = User.objects.create_user(**data)
        artist = Artist(user=user)
        artist.save()
        
