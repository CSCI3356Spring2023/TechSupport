from django.urls import path
from . import views

urlpatterns = [
    path('login_home', views.login_home, name='login'),
]