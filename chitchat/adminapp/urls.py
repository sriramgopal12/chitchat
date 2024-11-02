from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpagecall, name='loginpagecall'),
    path('register/', views.registerpagecall, name='registerpagecall'),
    path('logout/', views.logout_view, name='logout'),
    path('chitchat/', views.chitchat, name='chitchat'),  # Add this line
]