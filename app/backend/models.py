from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms

# Create your models here.
class Snippet(models.Model):
    language_choices = [(str(i), language) for i, language in enumerate(['bash', 'python'])]
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50)
    body = models.TextField()
    language = models.CharField(max_length=25,choices=language_choices, blank=True, null=True)

    def __str__(self):
        return f'{self.language_choices[int(self.language)][1]}: {self.name}'
    
    def __repr_(self):
        return self.__str__()