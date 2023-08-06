from django.urls import path
from home import views

urlpatterns = [
    path('', views.homeAbout),
    path('about', views.homeAbout),
    path('shortener', views.homeShortener),
    path('shorten', views.shorten, name='shorten'),
    path('<str:id>', views.redirectUrl)
]
