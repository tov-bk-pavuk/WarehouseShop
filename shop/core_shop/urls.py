from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path


from usr_auth import views


urlpatterns = [
    path('', views.user_login, name='home'),
    path('users/', include('usr_auth.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
]