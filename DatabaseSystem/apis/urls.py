from django.urls import include, path
from knox import views as knox_views
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'records', RecordViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', LogoutAPI.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('register/', RegisterAPI.as_view(), name='register'),
]
