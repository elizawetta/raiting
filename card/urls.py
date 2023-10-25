from django.urls import path
from . import views
urlpatterns = [  
    path('user/', views.user, name='card-user'),
    path('', views.home, name='card-home'),
    path('calendar/', views.calendar, name='card-calendar'),
    path('about-us/', views.about_us, name='card-about-us'),
    path('gallery/', views.gallery, name='card-gallery'),
]
