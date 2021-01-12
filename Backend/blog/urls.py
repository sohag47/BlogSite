from django.urls import path

from . import views
from .views import (create_category, create_post,delete_category,
                    delete_comments, delete_post, detail_post, list_category,
                    list_post, update_category, update_comments, update_post
)
urlpatterns = [
    # TODO for testing home page
    path('', views.list_post, name='home'),
    
    # TODO   Comment CURD URL:
    # Create operation:
    path("create_category/", views.create_category,
         name="create_category"),
    # Update  operation:
    path('update_category/<id>/',
         views.update_category, name='update_category'),
    # Delete operation:
    path('delete_category/<id>/',
         views.delete_category, name='delete_category'),
    # Read operation:
    path('list_category/', views.list_category,
         name='list_category'),

    # TODO Post  CURD Operation:
    # Create operation:
    path("create_post/", views.create_post, name="create_post"),
    # Read operation:
    path('list_post/', views.list_post,
         name='list_post'),
    # Update  operation:
    path('update_post/<id>/',
         views.update_post, name='update_post'),
    # Delete operation:
    path('delete_post/<id>/',
         views.delete_post, name='delete_post'),
    # Detail Post:
    path('detail_post/<id>/', views.detail_post, name='detail_post'),

    # TODO  comments  CURD Operation:
    # Update  operation:
    path('update_comments/<id>/',
         views.update_comments, name='update_comments'),
    # Delete operation:
    path('delete_comments/<id>/',
         views.delete_comments, name='delete_comments'),
]
