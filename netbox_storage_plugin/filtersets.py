# storage/filters.py
from django_filters import FilterSet, CharFilter, NumberFilter, ChoiceFilter, BooleanFilter
from django.contrib.contenttypes.models import ContentType
from netbox.filtersets import NetBoxModelFilterSet
from .models import ( 
    Disk, DiskSet, LogicalDrive, Filesystem, Share, SANVolume, ObjectStorage, VMDisk,
    INTERFACE_CHOICES, DISK_SPEED_CHOICES, DISKSET_TYPE_CHOICES, RAID_LEVEL_CHOICES,
    LOGICAL_DRIVE_CHOICES, FS_TYPE_CHOICES, SHARE_PROTOCOL_CHOICES, SAN_PROTOCOL_CHOICES,
    PROVIDER_CHOICES, FORMAT_CHOICES, PROVISIONING_CHOICES, CONTROLLER_CHOICES)

# Existing FilterSets (unchanged)
class DiskFilterSet(NetBoxModelFilterSet):
    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    size = NumberFilter(lookup_expr='exact')
    interface = ChoiceFilter(choices=INTERFACE_CHOICES)
    speed = ChoiceFilter(choices=DISK_SPEED_CHOICES)
    part_number = CharFilter(lookup_expr='icontains')
    serial_number = CharFilter(lookup_expr='icontains')
    firmware_version = CharFilter(lookup_expr='icontains')
    wwn = CharFilter(lookup_expr='icontains')

    # Filter by associated object (GenericForeignKey)
    associated_object_type = CharFilter(method='filter_associated_object_type')
    associated_object_id = NumberFilter(method='filter_associated_object_id')

    def filter_associated_object_type(self, queryset, name, value):
        try:
            content_type = ContentType.objects.get(model=value.lower())
            return queryset.filter(associated_object_type=content_type)
        except ContentType.DoesNotExist:
            return queryset.none()

    def filter_associated_object_id(self, queryset, name, value):
        return queryset.filter(associated_object_id=value)

    class Meta:
        model = Disk
        fields = ['name', 'description', 'size', 'interface', 'speed', 'part_number', 'serial_number', 'firmware_version', 'wwn', 'associated_object_type', 'associated_object_id']

class DiskSetFilterSet(NetBoxModelFilterSet):
    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    type = ChoiceFilter(choices=DISKSET_TYPE_CHOICES)  
    raid_level = CharFilter(choices=RAID_LEVEL_CHOICES)
    disk_count = NumberFilter(lookup_expr='exact')

    class Meta:
        model = DiskSet
        fields = ['name', 'description', 'type', 'raid_level', 'disk_count']

class LogicalDriveFilterSet(NetBoxModelFilterSet):
    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    type = ChoiceFilter(choices=LOGICAL_DRIVE_CHOICES)
    identifier = CharFilter(lookup_expr='icontains')

    class Meta:
        model = LogicalDrive
        fields = ['name', 'description', 'type', 'identifier']

class FilesystemFilterSet(NetBoxModelFilterSet):
    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    fs_type = ChoiceFilter(choices=FS_TYPE_CHOICES)
    mount_point = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Filesystem
        fields = ['name', 'description', 'fs_type', 'mount_point']

# New FilterSets for Share, SanVolume, and VirtualDisk
class ShareFilterSet(NetBoxModelFilterSet):
    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    protocol = ChoiceFilter(choices=SHARE_PROTOCOL_CHOICES) 
    path = CharFilter(lookup_expr='icontains')
    size = NumberFilter(lookup_expr='exact')

    class Meta:
        model = Share
        fields = ['name', 'description', 'protocol', 'path', 'size']

class SANVolumeFilterSet(NetBoxModelFilterSet):
    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    lun = NumberFilter(lookup_expr='exact')
    size = NumberFilter(lookup_expr='exact')
    protocol = ChoiceFilter(choices=SAN_PROTOCOL_CHOICES)  

    class Meta:
        model = SANVolume
        fields = ['name', 'description', 'lun', 'size', 'protocol']

class ObjectStorageFilterSet(NetBoxModelFilterSet):
    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    provider = ChoiceFilter(choices=PROVIDER_CHOICES) 
    region = CharFilter(lookup_expr='icontains')
    bucket_name = CharFilter(lookup_expr='icontains')

    class Meta:
        model = ObjectStorage
        fields = ['name', 'description', 'provider', 'region', 'bucket_name']

class VMDiskFilterSet(NetBoxModelFilterSet):
    name = CharFilter(lookup_expr='icontains')
    description = CharFilter(lookup_expr='icontains')
    size = NumberFilter(lookup_expr='exact')
    provisioning = ChoiceFilter(choices=PROVISIONING_CHOICES) 
    controller = ChoiceFilter(Choices=CONTROLLER_CHOICES)
    format = ChoiceFilter(choices=FORMAT_CHOICES)

    class Meta:
        model = VMDisk
        fields = ['name', 'description', 'size', 'type', 'vm_id']