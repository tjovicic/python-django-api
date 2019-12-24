from rest_framework.routers import SimpleRouter

from .views import UserViewSet, PostViewSet


router = SimpleRouter()
router.register('users', UserViewSet)
router.register('', PostViewSet)

urlpatterns = router.urls
