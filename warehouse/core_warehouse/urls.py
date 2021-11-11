from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path

from rest_framework import routers, serializers, viewsets

from usr_auth import views


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.user_login, name='home'),
    path('base/', views.base, name='base'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('usr_auth.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
