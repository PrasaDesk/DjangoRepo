from userData.api.view import userViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', userViewSet, base_name='userData')
urlpatterns = router.urls
