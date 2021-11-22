from django import forms
from django.contrib.auth.models import User

from users.models import Artist

class SignUpForm(forms.Form):
    username = forms.CharField(
        min_length=5,
        max_length=200,
        required=True,
        error_messages= {
            "required": "Se requiere el nombre del artista",
            "unique": "El nombre de artista ya está en uso"
        }
    )
    email = forms.CharField(
        widget=forms.EmailInput(),
        required=True,
        error_messages={
            "required": "Se requiere el email del artista",
            "unique": "El email del artista ya está en uso"
        }
    )
    password = forms.CharField(
        min_length=5,
        required=True,
        widget=forms.PasswordInput(),
        error_messages={
            "required": "Por favor ingresa una contraseña"
        }
    )

    def clean_username(self):
        """Ensure if artist name is unique"""
        username = self.cleaned_data["username"]
        username_taken = User.objects.filter(username=username).exists()

        if username_taken:
            raise forms.ValidationError("Ese nombre ya está en uso")
        
        return username
    
    def save(self):
        """save object"""
        data = self.cleaned_data
        
        user = User.objects.create_user(**data)
        artist = Artist(user=user)
        artist.save()

        return artist


class LoginForm(forms.Form):
    """Handle login required fields"""

    email = forms.EmailField()
    password = forms.CharField()