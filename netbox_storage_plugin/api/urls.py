from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'disks', views.DiskViewSet, basename = 'disk')
router.register(r'disk-sets', views.DiskSetViewSet)
router.register(r'logical-drives', views.LogicalDriveViewSet)
router.register(r'filesystems', views.FilesystemViewSet)
router.register(r'shares', views.ShareViewSet)
router.register(r'san-volumes', views.SANVolumeViewSet)
router.register(r'object-storages', views.ObjectStorageViewSet)
router.register(r'virtual-disks', views.VMDiskViewSet)

urlpatterns = router.urls