from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Snippet
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        name=request.data['name']
        snippet = Snippet.objects.get(name=name)
        
        return Response(snippet.to_json())

    def put(self, request, format=None):
        print(request.data)
        data = request.data
        print(data['name'])
        snippet = Snippet(
            name=data['name'],
            body=data['body'],
            created_by=request.user
        )
        snippet.save()
        return Response(snippet.to_json())

    def delete(self, request, format=None):
        data = request.data
        snippet = Snippet.objects.get(name=data['name'])
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    