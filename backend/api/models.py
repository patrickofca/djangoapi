"""
This module defines the models for the API, including the Note model.
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Note(models.Model):
    """Class representing a note"""
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return str(self.title)
