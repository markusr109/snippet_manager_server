from . import views
from django.urls import path

urlpatterns = [
    path('snippet/', views.SnippetDetail.as_view()),
    path('snippets/', views.SnippetList.as_view(actions={'get':'list'}))
]
