from rest_framework.routers import DefaultRouter
from .views import VolumeViewSet

router = DefaultRouter()
router.register(r'volumes', VolumeViewSet)

urlpatterns = router.urls