from .serializers import SnippetSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .models import Snippet

class SnippetList(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = SnippetSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', None)
        queryset = Snippet.objects.filter(name=name)
        return queryset
