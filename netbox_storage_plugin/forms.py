from netbox.forms import NetBoxModelForm
from . import models

class DiskForm(NetBoxModelForm):
    class Meta:
        model = models.Disk
        fields = ['name', 'description', 'size', 'parent_content_type', 'parent_object_id', 'content_type', 'object_id', 'interface', 'speed']

class DiskSetForm(NetBoxModelForm):
    class Meta:
        model = models.DiskSet
        fields = ['name', 'description', 'size', 'parent_content_type', 'parent_object_id', 'content_type', 'object_id', 'type', 'raid_level', 'disk_count']

class LogicalDriveForm(NetBoxModelForm):
    class Meta:
        model = models.LogicalDrive
        fields = ['name', 'description', 'size', 'parent_content_type', 'parent_object_id', 'content_type', 'object_id', 'type', 'identifier']

class FilesystemForm(NetBoxModelForm):
    class Meta:
        model = models.Filesystem
        fields = ['name', 'description', 'size', 'parent_content_type', 'parent_object_id', 'content_type', 'object_id', 'fs_type', 'mount_point']

class ShareForm(NetBoxModelForm):
    class Meta:
        model = models.Share
        fields = ['name', 'description', 'size', 'parent_content_type', 'parent_object_id', 'content_type', 'object_id', 'protocol', 'export_path']

class SANVolumeForm(NetBoxModelForm):
    class Meta:
        model = models.SANVolume
        fields = ['name', 'description', 'size', 'parent_content_type', 'parent_object_id', 'content_type', 'object_id', 'protocol', 'target', 'lun_id']

class ObjectStorageForm(NetBoxModelForm):
    class Meta:
        model = models.ObjectStorage
        fields = ['name', 'description', 'size', 'parent_content_type', 'parent_object_id', 'content_type', 'object_id', 'provider', 'region', 'bucket_name']

class VMDiskForm(NetBoxModelForm):
    class Meta:
        model = models.VMDisk
        fields = ['name', 'description', 'size', 'parent_content_type', 'parent_object_id', 'content_type', 'object_id', 'format', 'provisioning', 'controller', 'path']