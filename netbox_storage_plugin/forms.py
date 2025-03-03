from . import models
from django.contrib.contenttypes.models import ContentType
from utilities.forms.fields import ContentTypeChoiceField
from netbox.forms import NetBoxModelForm, NetBoxModelImportForm
from django import forms
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

class DiskForm(NetBoxModelForm):
    associated_object_type = ContentTypeChoiceField(
        queryset=ContentType.objects.all().order_by('app_label', 'model'),
        required=False,
        label='Associated Object Type'
    )
    
    associated_object_id = forms.CharField(
        required=False,
        label='Associated Object',
        help_text='Associated Object ID'
    )
       
    content_type = ContentTypeChoiceField(
        queryset=ContentType.objects.all().order_by('app_label', 'model'),
        required=False,
        label='Parent Object Type'
    )
    
    parent_object_id = forms.CharField(
        required=False,
        label='Parent Object',
        help_text='Parent Object ID.'
    )
    
    class Meta:
        model = models.Disk
        fields = ['name', 'description', 'size', 'part_number', 'serial_number', 'wwn', 'firmware_version', 'interface', 'speed']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['content_type'].queryset = ContentType.objects.filter(
            Q(app_label='netbox_storage_plugin', model='disk') |
            Q(app_label='netbox_storage_plugin', model='diskset') |
            Q(app_label='netbox_storage_plugin', model='logicaldisk') |
            Q(app_label='netbox_storage_plugin', model='filesystem') |
            Q(app_label='netbox_storage_plugin', model='share') |
            Q(app_label='netbox_storage_plugin', model='sanvolme') |
            Q(app_label='netbox_storage_plugin', model='objectstorage') |
            Q(app_label='netbox_storage_plugin', model='virtualdisk')
        )
        self.fields['associated_object_type'].queryset = ContentType.objects.filter(
            Q(app_label='dcim', model='device') |
            Q(app_label='virtualization', model='cluster') |
            Q(app_label='virtualization', model='virtualmachine') |
            Q(app_label='virtualization', model='virtualdisk')
        )
        
    def clean(self):
        cleaned_data = super().clean()
        ct = cleaned_data.get('content_type')
        obj_id = cleaned_data.get('object_id')
        if ct and obj_id:
            try:
                ct.get_object_for_this_type(pk=obj_id)
            except ObjectDoesNotExist:
                raise forms.ValidationError("Invalid related object.")
        return cleaned_data

class DiskImportForm(NetBoxModelImportForm):
    class Meta:
        model = models.Disk
        fields = ['name', 'description', 'size', 'content_type', 'object_id', 'part_number', 'serial_number', 'wwn', 'firmware_version', 'interface', 'speed']

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