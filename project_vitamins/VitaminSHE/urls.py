from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='VitaminSHE-home'),
    path('signup/', views.signup, name='VitaminSHE-signup'),
    path('login/', views.login, name='VitaminSHE-login'),
    path('healthcheck/', views.healthcheck, name='VitaminSHE-healthcheck'),
    path('food/', views.login, name='VitaminSHE-food'),
    path('book/', views.login, name='VitaminSHE-book'),
    path('why/', views.login, name='VitaminSHE-why'),
]
