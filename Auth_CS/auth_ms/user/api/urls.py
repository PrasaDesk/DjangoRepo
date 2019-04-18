from django.urls import path
from .views import UserRecordView, UserRecord_View, register_user, register_user_alldata


urlpatterns = [
    path('list/', UserRecordView.as_view()),
    path('', UserRecord_View.as_view()),
    path('registration/', register_user_alldata),
    path('register/', register_user),
]
