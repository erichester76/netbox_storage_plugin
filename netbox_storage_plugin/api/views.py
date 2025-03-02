from rest_framework.viewsets import ModelViewSet
from . import serializers 
from .. import models 

# Disk ViewSet
class DiskViewSet(ModelViewSet):
    queryset = models.Disk.objects.all()
    serializer_class = serializers.DiskSerializer

# DiskSet ViewSet
class DiskSetViewSet(ModelViewSet):
    queryset = models.DiskSet.objects.all()
    serializer_class = serializers.DiskSetSerializer

# LogicalDrive ViewSet
class LogicalDriveViewSet(ModelViewSet):
    queryset = models.LogicalDrive.objects.all()
    serializer_class = serializers.LogicalDriveSerializer

# Filesystem ViewSet
class FilesystemViewSet(ModelViewSet):
    queryset = models.Filesystem.objects.all()
    serializer_class = serializers.FilesystemSerializer

# Share ViewSet
class ShareViewSet(ModelViewSet):
    queryset = models.Share.objects.all()
    serializer_class = serializers.ShareSerializer

# SANVolume ViewSet
class SANVolumeViewSet(ModelViewSet):
    queryset = models.SANVolume.objects.all()
    serializer_class = serializers.SANVolumeSerializer

# ObjectStorage ViewSet
class ObjectStorageViewSet(ModelViewSet):
    queryset = models.ObjectStorage.objects.all()
    serializer_class = serializers.ObjectStorageSerializer

# VMDisk ViewSet
class VMDiskViewSet(ModelViewSet):
    queryset = models.VMDisk.objects.all()
    serializer_class = serializers.VMDiskSerializer