from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django import forms

# Create your models here.
class Snippet(models.Model):
    language_choices = [(str(i), language) for i, language in enumerate(['bash', 'python'])]
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=50, unique=True)
    body = models.TextField()
    language = models.CharField(max_length=25, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'
    
    def __repr_(self):
        return self.__str__()
    
    def to_json(self):
        data = self.__dict__
        # try:
        #     del(data['_state'])
        # except:
        #     print(data)
        return {
            'created_by': self.created_by.id,
            'created_at': self.created_at,
            'name': self.name,
            'body': self.body,
            'language': self.language
        }