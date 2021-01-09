from django.urls import path

from . import views
from .views import create_post, list_post

urlpatterns = [
    path('', views.list_post, name='home'),
    # Create operation:
    path("create_post/", views.create_post, name="create_post"),
]
