import django_tables2 as tables
from netbox.tables import NetBoxTable
from . import models

# Table for Disk model
class DiskTable(NetBoxTable):
    name = tables.Column(linkify=True)
    interface = tables.Column()
    speed = tables.Column()
    size = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.Disk
        fields = ('name', 'interface', 'speed', 'size', 'description')

# Table for DiskSet model
class DiskSetTable(NetBoxTable):
    name = tables.Column(linkify=True)
    type = tables.Column()
    raid_level = tables.Column()
    disk_count = tables.Column()
    size = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.DiskSet
        fields = ('name', 'type', 'raid_level', 'disk_count', 'size', 'description')

# Table for LogicalDrive model
class LogicalDriveTable(NetBoxTable):
    name = tables.Column(linkify=True)
    type = tables.Column()
    identifier = tables.Column()
    size = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.LogicalDrive
        fields = ('name', 'type', 'identifier', 'size', 'description')

# Table for Filesystem model
class FilesystemTable(NetBoxTable):
    name = tables.Column(linkify=True)
    fs_type = tables.Column()
    mount_point = tables.Column()
    size = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.Filesystem
        fields = ('name', 'fs_type', 'mount_point', 'size', 'description')

# Table for Share model
class ShareTable(NetBoxTable):
    name = tables.Column(linkify=True)
    protocol = tables.Column()
    export_path = tables.Column()
    size = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.Share
        fields = ('name', 'protocol', 'export_path', 'size', 'description')

# Table for SANVolume model
class SANVolumeTable(NetBoxTable):
    name = tables.Column(linkify=True)
    protocol = tables.Column()
    target = tables.Column()
    lun_id = tables.Column()
    size = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.SANVolume
        fields = ('name', 'protocol', 'target', 'lun_id', 'size', 'description')

# Table for ObjectStorage model
class ObjectStorageTable(NetBoxTable):
    name = tables.Column(linkify=True)
    provider = tables.Column()
    region = tables.Column()
    bucket_name = tables.Column()
    size = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.ObjectStorage
        fields = ('name', 'provider', 'region', 'bucket_name', 'size', 'description')

# Table for VMDisk model
class VMDiskTable(NetBoxTable):
    name = tables.Column(linkify=True)
    format = tables.Column()
    provisioning = tables.Column()
    controller = tables.Column()
    path = tables.Column()
    size = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = models.VMDisk
        fields = ('name', 'format', 'provisioning', 'controller', 'path', 'size', 'description')