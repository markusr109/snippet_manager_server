from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Snippet
from django.contrib.auth.models import User
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics
from django.db.utils import IntegrityError

class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        name = request.data['name']
        try:
            snippet = Snippet.objects.get(name=name)
            return Response(snippet.to_json(), status=status.HTTP_200_OK)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        

    def put(self, request, format=None):
        data = request.data
        snippet = Snippet(
            name=data['name'],
            body=data['body'],
            language=data['language'],
            created_by=request.user
        )
        try:
            snippet.save()
            return Response(snippet.to_json(), status=status.HTTP_201_CREATED)
        except IntegrityError as e:
            return Response({'status': 'failed', 'e':str(e)}, status=status.HTTP_409_CONFLICT)

    def delete(self, request, format=None):
        data = request.data
        name = data['name']
        try:
            Snippet.objects.get(name=name).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Snippet.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    