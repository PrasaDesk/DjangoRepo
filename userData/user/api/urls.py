from django.urls import path
from django.contrib.auth.models import User
from .views import UserRecordView, UserCreateView

urlpatterns = [
    path('', UserRecordView.as_view()),
    # path("<pk>/", UserRecordRetriveView.as_view()),
    path('register/', UserCreateView.as_view())
]
