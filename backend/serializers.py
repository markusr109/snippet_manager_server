from rest_framework import routers, serializers, viewsets
from .models import *

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        fields = ['created_at', 'name', 'body', 'language']
