from django.core.exceptions import ValidationError

from . import models

def validate_title(value):
    blog_title = models.Post.objects.all()

    for titles in blog_title:
        if value == titles.title:
            message = 'JUDUL TIDAK BOLEH SAMA'
            raise ValidationError(message)