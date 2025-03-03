from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import ( 
    Disk, DiskSet, LogicalDrive, Filesystem, Share, SANVolume, ObjectStorage, VMDisk,
    INTERFACE_CHOICES, DISK_SPEED_CHOICES, DISKSET_TYPE_CHOICES, RAID_LEVEL_CHOICES,
    LOGICAL_DRIVE_CHOICES, FS_TYPE_CHOICES, SHARE_PROTOCOL_CHOICES, SAN_PROTOCOL_CHOICES,
    PROVIDER_CHOICES, FORMAT_CHOICES, PROVISIONING_CHOICES, CONTROLLER_CHOICES)

# Serializer for Disk model
class DiskSerializer(NetBoxModelSerializer):
    
    interface = serializers.ChoiceField(choices=INTERFACE_CHOICES)
    speed = serializers.ChoiceField(choices=DISK_SPEED_CHOICES)

    class Meta:
        model = Disk
        fields = '__all__'

# Serializer for DiskSet model
class DiskSetSerializer(NetBoxModelSerializer):
    
    type = serializers.ChoiceField(choices=DISKSET_TYPE_CHOICES)
    raid_level = serializers.ChoiceField(choices=RAID_LEVEL_CHOICES)
    disk_count = serializers.IntegerField()

    class Meta:
        model = DiskSet
        fields = '__all__'

# Serializer for LogicalDrive model
class LogicalDriveSerializer(NetBoxModelSerializer):
    
    type = serializers.ChoiceField(choices=LOGICAL_DRIVE_CHOICES)
    identifier = serializers.CharField()

    class Meta:
        model = LogicalDrive
        fields = '__all__'

# Serializer for Filesystem model
class FilesystemSerializer(NetBoxModelSerializer):

    fs_type = serializers.ChoiceField(choices=FS_TYPE_CHOICES)
    mount_point = serializers.CharField()

    class Meta:
        model = Filesystem
        fields = '__all__'

# Serializer for Share model
class ShareSerializer(NetBoxModelSerializer):

    protocol = serializers.ChoiceField(choices=SHARE_PROTOCOL_CHOICES)
    export_path = serializers.CharField()

    class Meta:
        model = Share
        fields = '__all__'

# Serializer for SANVolume model
class SANVolumeSerializer(NetBoxModelSerializer):
 
    protocol = serializers.ChoiceField(choices=SAN_PROTOCOL_CHOICES)
    target = serializers.CharField()
    lun_id = serializers.IntegerField()

    class Meta:
        model = SANVolume
        fields = '__all__'

# Serializer for ObjectStorage model
class ObjectStorageSerializer(NetBoxModelSerializer):

    provider = serializers.ChoiceField(choices=PROVIDER_CHOICES)
    region = serializers.CharField()
    bucket_name = serializers.CharField()

    class Meta:
        model = ObjectStorage
        fields = '__all__'

# Serializer for VMDisk model
class VMDiskSerializer(NetBoxModelSerializer):
    format = serializers.ChoiceField(choices=FORMAT_CHOICES)
    provisioning = serializers.ChoiceField(choices=PROVISIONING_CHOICES)
    controller = serializers.ChoiceField(choices=CONTROLLER_CHOICES)
    path = serializers.CharField()

    class Meta:
        model = VMDisk
        fields = '__all__'