from django.urls import path
from .views import login

"""
This URL file is for call the login api directly

http//:localhost:8000/login/

"""
urlpatterns = [
    path('', login),
]