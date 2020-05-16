from django.db import models

from . import validators

class Post(models.Model):
    title = models.CharField(max_length=100, validators=[validators.validate_title])
    body = models.TextField()
    email = models.EmailField(default ='admin@gmail.com')

    LIST_CHOICES = (
        ('olahraga','olahraga'), 
        ('kesehatan','kesehatan'), 
        ('unknown','unknown'), 
        )
    category = models.CharField(max_length=100, choices=LIST_CHOICES, default='unknown')

    def __str__(self):
        return "{}. {}".format(self.id, self.title)

