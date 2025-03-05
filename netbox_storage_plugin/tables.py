import django_tables2 as tables
from netbox.tables import NetBoxTable
from .models import (
    Disk, DiskSet, LogicalDrive, Filesystem, Share, SANVolume, ObjectStorage, VMDisk
)

def format_size(value):
    """
    Convert a byte value to a human-readable format (MB, GB, TB, PB).
    """
    if value is None or value == 0:
        return "N/A"
    
    # Define the units and their conversion factors (in bytes)
    units = [
        (1e18, 'EB'),
        (1e15, 'PB'),
        (1e12, 'TB'),
        (1e9, 'GB'), 
        (1e6, 'MB'), 
        (1e3, 'KB'), 
    ]
    
    for threshold, unit in units:
        if value >= threshold:
            formatted_value = value / threshold
            return f"{formatted_value:.2f} {unit}"
    
    return f"{value} B" 

class DiskTable(NetBoxTable):
    name = tables.Column(linkify=True)
    size = tables.Column()
    interface = tables.Column()
    speed = tables.Column()
    associated_object = tables.Column(
        verbose_name="Associated Object",
        accessor="associated_object",
        orderable=False,
        linkify=True,
    )
    class Meta(NetBoxTable.Meta):
        model = Disk
        fields = ('pk', 'name', 'description', 'part_number', 'serial_number', 'wwn', 'firmware_version', 'size', 'interface', 'speed', 'associated_object')
        default_columns = ('associated_object', 'name', 'description', 'part_number', 'size', 'interface', 'speed')

    def render_size(self, value):
        return format_size(value)

class DiskSetTable(NetBoxTable):
    name = tables.Column(linkify=True)
    size = tables.Column()
    type = tables.Column()
    raid_level = tables.Column()
    disk_count = tables.Column()
    associated_object = tables.Column(
        verbose_name="Associated Object",
        accessor="associated_object",
        orderable=False,
        linkify=True,
    )
    parent_object = tables.Column(
        verbose_name="Parent Object",
        accessor="parent_object",
        orderable=False,
        linkify=True,
    )
    
    class Meta(NetBoxTable.Meta):
        model = DiskSet
        fields = ('pk', 'name', 'size', 'type', 'raid_level', 'disk_count', 'description', 'parent_object', 'associated_object')
        default_columns = ('name', 'size', 'type', 'raid_level', 'disk_count', 'parent_object', 'associated_object')

    def render_size(self, value):
        return format_size(value)

class LogicalDriveTable(NetBoxTable):
    name = tables.Column(linkify=True)
    size = tables.Column()
    type = tables.Column()
    identifier = tables.Column()
    parent_object = tables.Column(
        verbose_name="Parent Object",
        accessor="parent_object",
        orderable=False,
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = LogicalDrive
        fields = ('pk', 'name', 'size', 'type', 'identifier', 'description', 'parent_object', 'associated_object')
        default_columns = ('name', 'size', 'type', 'identifier', 'parent_object', 'associated_object')

    def render_size(self, value):
        return format_size(value)

class FilesystemTable(NetBoxTable):
    name = tables.Column(linkify=True)
    size = tables.Column()
    fs_type = tables.Column()
    mount_point = tables.Column()
    associated_object = tables.Column(
        verbose_name="Associated Object",
        accessor="associated_object",
        orderable=False,
        linkify=True,
    )
    parent_object = tables.Column(
        verbose_name="Parent Object",
        accessor="parent_object",
        orderable=False,
        linkify=True,
    )
    
    class Meta(NetBoxTable.Meta):
        model = Filesystem
        fields = ('pk', 'name', 'size', 'fs_type', 'mount_point', 'description', 'parent_object', 'associated_object')
        default_columns = ('name', 'size', 'fs_type', 'mount_point', 'parent_object', 'associated_object')

    def render_size(self, value):
        return format_size(value)

class ShareTable(NetBoxTable):
    name = tables.Column(linkify=True)
    size = tables.Column()
    protocol = tables.Column()
    export_path = tables.Column()
    associated_object = tables.Column(
        verbose_name="Associated Object",
        accessor="associated_object",
        orderable=False,
        linkify=True,
    )
    parent_object = tables.Column(
        verbose_name="Parent Object",
        accessor="parent_object",
        orderable=False,
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = Share
        fields = ('pk', 'name', 'size', 'protocol', 'export_path', 'description', 'parent_object', 'associated_object')
        default_columns = ('name', 'size', 'protocol', 'export_path', 'parent_object', 'associated_object')

    def render_size(self, value):
        return format_size(value)

class SANVolumeTable(NetBoxTable):
    name = tables.Column(linkify=True)
    size = tables.Column()
    protocol = tables.Column()
    target = tables.Column()
    lun_id = tables.Column()
    associated_object = tables.Column(
        verbose_name="Associated Object",
        accessor="associated_object",
        orderable=False,
        linkify=True,
    )
    parent_object = tables.Column(
        verbose_name="Parent Object",
        accessor="parent_object",
        orderable=False,
        linkify=True,
    )
    
    class Meta(NetBoxTable.Meta):
        model = SANVolume
        fields = ('pk', 'name', 'size', 'protocol', 'target', 'lun_id', 'description', 'parent_object', 'associated_object')
        default_columns = ('name', 'size', 'protocol', 'target', 'lun_id', 'parent_object', 'associated_object')

    def render_size(self, value):
        return format_size(value)

class ObjectStorageTable(NetBoxTable):
    name = tables.Column(linkify=True)
    size = tables.Column()
    provider = tables.Column()
    region = tables.Column()
    bucket_name = tables.Column()
    associated_object = tables.Column(
        verbose_name="Associated Object",
        accessor="associated_object",
        orderable=False,
        linkify=True,
    )
    parent_object = tables.Column(
        verbose_name="Parent Object",
        accessor="parent_object",
        orderable=False,
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = ObjectStorage
        fields = ('pk', 'name', 'size', 'provider', 'region', 'bucket_name', 'description', 'parent_object', 'associated_object')
        default_columns = ('name', 'size', 'provider', 'region', 'bucket_name', 'parent_object', 'associated_object')

    def render_size(self, value):
        return format_size(value)
    
class VMDiskTable(NetBoxTable):
    name = tables.Column(linkify=True)
    size = tables.Column()
    format = tables.Column()
    provisioning = tables.Column()
    controller = tables.Column()
    associated_object = tables.Column(
        verbose_name="Associated Object",
        accessor="associated_object",
        orderable=False,
        linkify=True,
    )
    parent_object = tables.Column(
        verbose_name="Parent Object",
        accessor="parent_object",
        orderable=False,
        linkify=True,
    )

    class Meta(NetBoxTable.Meta):
        model = VMDisk
        fields = ('pk', 'name', 'size', 'format', 'provisioning', 'controller', 'path', 'description', 'parent_object', 'associated_object')
        default_columns = ('name', 'size', 'format', 'provisioning', 'controller', 'parent_object', 'associated_object')
    
    def render_size(self, value):
        return format_size(value)