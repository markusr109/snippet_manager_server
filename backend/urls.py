from . import views
from django.urls import path

urlpatterns = [
    path('test/', views.SnippetList.as_view())
]