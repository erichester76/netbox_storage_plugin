from netbox.api.routers import NetBoxRouter
from . import views

router = NetBoxRouter()
router.register(r'disks', views.DiskViewSet)
router.register(r'disksets', views.DiskSetViewSet)
router.register(r'logicaldrives', views.LogicalDriveViewSet)
router.register(r'filesystems', views.FilesystemViewSet)
router.register(r'shares', views.ShareViewSet)
router.register(r'sanvolumes', views.SANVolumeViewSet)
router.register(r'objectstorages', views.ObjectStorageViewSet)
router.register(r'virtualdisks', views.VMDiskViewSet)

urlpatterns = router.urls