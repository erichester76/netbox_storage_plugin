# storage/api/views.py
from netbox.api.viewsets import NetBoxModelViewSet
from ..models import Disk, DiskSet, LogicalDrive, Filesystem, Share, SANVolume, ObjectStorage, VMDisk
from .serializers import DiskSerializer, DiskSetSerializer, LogicalDriveSerializer, FilesystemSerializer, ShareSerializer, SANVolumeSerializer, ObjectStorageSerializer, VMDiskSerializer
from ..filtersets import DiskFilterSet, DiskSetFilterSet, LogicalDriveFilterSet, FilesystemFilterSet, ShareFilterSet, SANVolumeFilterSet, ObjectStorageFilterSet, VMDiskFilterSet

class DiskViewSet(NetBoxModelViewSet):
    queryset = Disk.objects.all()
    serializer_class = DiskSerializer
    filterset_class = DiskFilterSet

class DiskSetViewSet(NetBoxModelViewSet):
    queryset = DiskSet.objects.all()
    serializer_class = DiskSetSerializer
    filterset_class = DiskSetFilterSet

class LogicalDriveViewSet(NetBoxModelViewSet):
    queryset = LogicalDrive.objects.all()
    serializer_class = LogicalDriveSerializer
    filterset_class = LogicalDriveFilterSet

class FilesystemViewSet(NetBoxModelViewSet):
    queryset = Filesystem.objects.all()
    serializer_class = FilesystemSerializer
    filterset_class = FilesystemFilterSet

class ShareViewSet(NetBoxModelViewSet):
    queryset = Share.objects.all()
    serializer_class = ShareSerializer
    filterset_class = ShareFilterSet

class ObjectStorageViewSet(NetBoxModelViewSet):
    queryset = ObjectStorage.objects.all()
    serializer_class = ObjectStorageSerializer
    filterset_class = ObjectStorageFilterSet

class SanVolumeViewSet(NetBoxModelViewSet):
    queryset = SANVolume.objects.all()
    serializer_class = SANVolumeSerializer
    filterset_class = SANVolumeFilterSet

class VirtualDiskViewSet(NetBoxModelViewSet):
    queryset = VMDisk.objects.all()
    serializer_class = VMDiskSerializer
    filterset_class = VMDiskFilterSet