from netbox.forms import NetBoxModelForm
from . import models
from netbox.forms.fields import DynamicModelChoiceField, ContentTypeChoiceField
from django import forms
from django.contrib.contenttypes.models import ContentType

class DiskForm(NetBoxModelForm):
    associated_object_type = ContentTypeChoiceField(
        queryset=ContentType.objects.all().order_by('app_label', 'model'),
        required=False,
        label='Associated Object Type'
    )
    
    associated_object_id = forms.CharField(
        required=False,
        label='Associated Object',
        help_text='Select an object of the chosen type.'
    )
       
    content_type = ContentTypeChoiceField(
        queryset=ContentType.objects.all().order_by('app_label', 'model'),
        required=False,
        label='Associated Object Type'
    )
    
    object_id = forms.CharField(
        required=False,
        label='Associated Object',
        help_text='Select an object of the chosen type.'
    )
    
    class Meta:
        model = models.Disk
        fields = ['name', 'description', 'size', 'parent_content_type', 'parent_object_id', 'associated_object', 'associated_object_type', 'associated_object_id', 'interface', 'speed']


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content_type'].queryset = ContentType.objects.filter(
            Q(app_label='dcim', model='device') |
            Q(app_label='virtualization', model='virtualmachine')
        )
        self.fields['associated_object_type'].queryset = ContentType.objects.filter(
            Q(app_label='dcim', model='device') |
            Q(app_label='virtualization', model='virtualmachine')
        )


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