"""Validator module"""
from django.core.exceptions import ValidationError

import os


def validate_image_extension(file):
    """Validates if uploaded file is an image"""
    extension = os.path.splitext(file.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.svg', '.jfif', '.pjpeg', '.pjp', '.webp']
    if not extension.lower() in valid_extensions:
        raise ValidationError('Unsopported file extension')
