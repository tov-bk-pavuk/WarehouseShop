from django.urls import path

from . import views

urlpatterns = [
    path('usr_login', views.user_login, name='usr_login'),
    path('logout', views.user_logout, name='usr_logout')
]
