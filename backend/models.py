from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Snippet(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    body = models.TextField()