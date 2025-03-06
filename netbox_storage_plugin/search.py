from netbox.search import SearchIndex, register_search
from .models import LogicalDrive, Filesystem, Share, Disk, DiskSet, SANVolume, ObjectStorage, VMDisk

@register_search
class DiskIndex(SearchIndex):
    model = Disk
    fields = (
        ('name', 100),
        ('description', 50),
        ('interface', 50),
        ('speed', 50),
        ('part_number', 50),
        ('serial_number', 50),
        ('firmware_version', 50),
        ('wwn', 50),
        ('state', 50),
    )

# LogicalDrive Search Index
@register_search
class LogicalDriveIndex(SearchIndex):
    model = LogicalDrive
    fields = (
        ('name', 100),  # Weight of 100 for high relevance
        ('description', 50),  # Weight of 50 for lower relevance
        ('type', 50),
        ('identifier', 50),
        ('state', 50),
    )

# Filesystem Search Index
@register_search
class FilesystemIndex(SearchIndex):
    model = Filesystem
    fields = (
        ('name', 100),
        ('description', 50),
        ('fs_type', 50),
        ('mount_point', 50),
        ('state', 50),
    )

# Share Search Index
@register_search
class ShareIndex(SearchIndex):
    model = Share
    fields = (
        ('name', 100),
        ('description', 50),
        ('protocol', 50),
        ('state', 50),
    )

# DiskSet Search Index
@register_search
class DiskSetIndex(SearchIndex):
    model = DiskSet
    fields = (
        ('name', 100),
        ('description', 50),
        ('state', 50),
    )

# SanVolume Search Index
@register_search
class SANVolumeIndex(SearchIndex):
    model = SANVolume
    fields = (
        ('name', 100),
        ('description', 50),
        ('protocol', 50),
        ('state', 50),
    )

# ObjectStorage Search Index
@register_search
class ObjectStorageIndex(SearchIndex):
    model = ObjectStorage
    fields = (
        ('name', 100),
        ('description', 50),
        ('bucket_name', 50),
        ('provider', 50),
        ('state', 50),
    )

# VMDisk Search Index
@register_search
class VMDiskIndex(SearchIndex):
    model = VMDisk
    fields = (
        ('name', 100),
        ('description', 50),
        ('state', 50),
    )