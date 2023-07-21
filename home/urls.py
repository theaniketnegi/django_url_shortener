from django.urls import path
from home import views

urlpatterns = [
    path('', views.home),
    path('shorten', views.shorten, name='shorten'),
    path('<str:pk>', views.redirectUrl)
]
