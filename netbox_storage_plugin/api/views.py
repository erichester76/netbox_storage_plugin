from netbox.api.viewsets import NetBoxModelViewSet
from . import serializers 
from .. import models 

# Disk ViewSet
class DiskViewSet(NetBoxModelViewSet):
    queryset = models.Disk.objects.all()
    serializer_class = serializers.DiskSerializer

# DiskSet ViewSet
class DiskSetViewSet(NetBoxModelViewSet):
    queryset = models.DiskSet.objects.all()
    serializer_class = serializers.DiskSetSerializer

# LogicalDrive ViewSet
class LogicalDriveViewSet(NetBoxModelViewSet):
    queryset = models.LogicalDrive.objects.all()
    serializer_class = serializers.LogicalDriveSerializer

# Filesystem ViewSet
class FilesystemViewSet(NetBoxModelViewSet):
    queryset = models.Filesystem.objects.all()
    serializer_class = serializers.FilesystemSerializer

# Share ViewSet
class ShareViewSet(NetBoxModelViewSet):
    queryset = models.Share.objects.all()
    serializer_class = serializers.ShareSerializer

# SANVolume ViewSet
class SANVolumeViewSet(NetBoxModelViewSet):
    queryset = models.SANVolume.objects.all()
    serializer_class = serializers.SANVolumeSerializer

# ObjectStorage ViewSet
class ObjectStorageViewSet(NetBoxModelViewSet):
    queryset = models.ObjectStorage.objects.all()
    serializer_class = serializers.ObjectStorageSerializer

# VMDisk ViewSet
class VMDiskViewSet(NetBoxModelViewSet):
    queryset = models.VMDisk.objects.all()
    serializer_class = serializers.VMDiskSerializer