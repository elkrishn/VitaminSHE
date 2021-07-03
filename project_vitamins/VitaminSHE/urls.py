from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='VitaminSHE-home'),
    path('about/', views.about, name='VitaminSHE-about'),
]

