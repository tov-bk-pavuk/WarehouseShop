from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path


from usr_auth.views import user_login


urlpatterns = [
    path('', user_login, name='home'),
    path('catalog/', include('catalog.urls')),
    path('cart/', include('cart.urls')),
    path('users/', include('usr_auth.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
]
