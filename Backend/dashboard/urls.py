from django.urls import path

from . import views
from .views import CreateUserInfo, dashboard

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('CreateUserInfo/', views.CreateUserInfo, name='CreateUserInfo'),
]
