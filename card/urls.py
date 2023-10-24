from django.urls import path
from . import views
urlpatterns = [  
    path('user/', views.user, name='card-user'),
    path('', views.home, name='card-home')
]
