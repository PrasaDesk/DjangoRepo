from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth', include('rest_framework.urls')),
    path('login/', include('user.api.loginURL')),
    path('users/', include('user.api.urls')),
    path('verify/', TokenVerifyView.as_view()),
]