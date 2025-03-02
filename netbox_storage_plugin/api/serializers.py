from netbox.api.serializers import NetBoxModelSerializer
from .. import models 

# Disk Serializer
class DiskSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.Disk
        fields = ('id', 'name', 'description', 'size', 'parent', 'associated_object', 'interface', 'speed')

# DiskSet Serializer
class DiskSetSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.DiskSet
        fields = ('id', 'name', 'description', 'size', 'parent', 'associated_object', 'type', 'raid_level', 'disk_count')

# LogicalDrive Serializer
class LogicalDriveSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.LogicalDrive
        fields = ('id', 'name', 'description', 'size', 'parent', 'associated_object', 'type', 'identifier')

# Filesystem Serializer
class FilesystemSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.Filesystem
        fields = ('id', 'name', 'description', 'size', 'parent', 'associated_object', 'fs_type', 'mount_point')

# Share Serializer
class ShareSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.Share
        fields = ('id', 'name', 'description', 'size', 'parent', 'associated_object', 'protocol', 'export_path')

# SANVolume Serializer
class SANVolumeSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.SANVolume
        fields = ('id', 'name', 'description', 'size', 'parent', 'associated_object', 'protocol', 'target', 'lun_id')

# ObjectStorage Serializer
class ObjectStorageSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.ObjectStorage
        fields = ('id', 'name', 'description', 'size', 'parent', 'associated_object', 'provider', 'region', 'bucket_name')

# VMDisk Serializer
class VMDiskSerializer(NetBoxModelSerializer):
    class Meta:
        model = models.VMDisk
        fields = ('id', 'name', 'description', 'size', 'parent', 'associated_object', 'format', 'provisioning', 'controller', 'path')