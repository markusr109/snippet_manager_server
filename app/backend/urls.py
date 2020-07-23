from . import views
from django.urls import path

urlpatterns = [
    path('', views.SnippetDetail.as_view())
]
