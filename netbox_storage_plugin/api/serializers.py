from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import (
    Disk, DiskSet, LogicalDrive, Filesystem, Share, SANVolume, ObjectStorage, VMDisk
)

# Serializer for Disk model
class DiskSerializer(NetBoxModelSerializer):
    """
    Serializer for Disk model, providing all fields for API interactions.
    """
    interface = serializers.ChoiceField(choices=Disk.INTERFACE_CHOICES)
    speed = serializers.ChoiceField(choices=Disk.SPEED_CHOICES)

    class Meta:
        model = Disk
        fields = '__all__'

# Serializer for DiskSet model
class DiskSetSerializer(NetBoxModelSerializer):
    """
    Serializer for DiskSet model, providing all fields for API interactions.
    """
    type = serializers.ChoiceField(choices=DiskSet.TYPE_CHOICES)
    raid_level = serializers.ChoiceField(choices=DiskSet.RAID_LEVEL_CHOICES)
    disk_count = serializers.IntegerField()

    class Meta:
        model = DiskSet
        fields = '__all__'

# Serializer for LogicalDrive model
class LogicalDriveSerializer(NetBoxModelSerializer):
    """
    Serializer for LogicalDrive model, providing all fields for API interactions.
    """
    type = serializers.ChoiceField(choices=LogicalDrive.TYPE_CHOICES)
    identifier = serializers.CharField()

    class Meta:
        model = LogicalDrive
        fields = '__all__'

# Serializer for Filesystem model
class FilesystemSerializer(NetBoxModelSerializer):
    """
    Serializer for Filesystem model, providing all fields for API interactions.
    """
    fs_type = serializers.ChoiceField(choices=Filesystem.FS_TYPE_CHOICES)
    mount_point = serializers.CharField()

    class Meta:
        model = Filesystem
        fields = '__all__'

# Serializer for Share model
class ShareSerializer(NetBoxModelSerializer):
    """
    Serializer for Share model, providing all fields for API interactions.
    """
    protocol = serializers.ChoiceField(choices=Share.PROTOCOL_CHOICES)
    export_path = serializers.CharField()

    class Meta:
        model = Share
        fields = '__all__'

# Serializer for SANVolume model
class SANVolumeSerializer(NetBoxModelSerializer):
    """
    Serializer for SANVolume model, providing all fields for API interactions.
    """
    protocol = serializers.ChoiceField(choices=SANVolume.PROTOCOL_CHOICES)
    target = serializers.CharField()
    lun_id = serializers.IntegerField()

    class Meta:
        model = SANVolume
        fields = '__all__'

# Serializer for ObjectStorage model
class ObjectStorageSerializer(NetBoxModelSerializer):
    """
    Serializer for ObjectStorage model, providing all fields for API interactions.
    """
    provider = serializers.ChoiceField(choices=ObjectStorage.PROVIDER_CHOICES)
    region = serializers.CharField()
    bucket_name = serializers.CharField()

    class Meta:
        model = ObjectStorage
        fields = '__all__'

# Serializer for VMDisk model
class VMDiskSerializer(NetBoxModelSerializer):
    """
    Serializer for VMDisk model, providing all fields for API interactions.
    """
    format = serializers.ChoiceField(choices=VMDisk.FORMAT_CHOICES)
    provisioning = serializers.ChoiceField(choices=VMDisk.PROVISIONING_CHOICES)
    controller = serializers.ChoiceField(choices=VMDisk.CONTROLLER_CHOICES)
    path = serializers.CharField()

    class Meta:
        model = VMDisk
        fields = '__all__'