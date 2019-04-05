from django.urls import path

from .view import RegisterUserListView, RegisterUserDetailView, RegisterUserCreateView, RegisterUserUpdateView, RegisterUserDeleteView

urlpatterns = [
    path('', RegisterUserListView.as_view()),
    path('register', RegisterUserCreateView.as_view()),
    path('<pk>/update', RegisterUserUpdateView.as_view()),
    path('<pk>/delete', RegisterUserDeleteView.as_view()),
    path('<pk>', RegisterUserDetailView.as_view())
]

# from userData.api.view import userViewSet
# from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'', userViewSet, base_name='userData')
# urlpatterns = router.urls
