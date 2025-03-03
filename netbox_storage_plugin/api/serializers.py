from netbox.api.serializers import NetBoxModelSerializer
from .. import models 

# Disk Serializer
class DiskSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.Disk
        fields = "__all__"

# DiskSet Serializer
class DiskSetSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.DiskSet
        fields = "__all__"

# LogicalDrive Serializer
class LogicalDriveSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.LogicalDrive
        fields = "__all__"

# Filesystem Serializer
class FilesystemSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.Filesystem
        fields = "__all__"

# Share Serializer
class ShareSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.Share
        fields = "__all__"

# SANVolume Serializer
class SANVolumeSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.SANVolume
        fields = "__all__"

# ObjectStorage Serializer
class ObjectStorageSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.ObjectStorage
        fields = "__all__"

# VMDisk Serializer
class VMDiskSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.VMDisk
        fields = "__all__"
