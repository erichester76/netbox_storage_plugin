from netbox.views import generic
from . import models, forms, tables
from django.contrib.contenttypes.models import ContentType
from utilities.views import register_model_view, ViewTab
from dcim.models import Device


class DiskListView(generic.ObjectListView):
    queryset = models.Disk.objects.all()
    table = tables.DiskTable

class DiskSetListView(generic.ObjectListView):
    queryset = models.DiskSet.objects.all()
    table = tables.DiskSetTable

class LogicalDriveListView(generic.ObjectListView):
    queryset = models.LogicalDrive.objects.all()
    table = tables.LogicalDriveTable

class FilesystemListView(generic.ObjectListView):
    queryset = models.Filesystem.objects.all()
    table = tables.FilesystemTable

class ShareListView(generic.ObjectListView):
    queryset = models.Share.objects.all()
    table = tables.ShareTable

class SANVolumeListView(generic.ObjectListView):
    queryset = models.SANVolume.objects.all()
    table = tables.SANVolumeTable

class ObjectStorageListView(generic.ObjectListView):
    queryset = models.ObjectStorage.objects.all()
    table = tables.ObjectStorageTable

class VMDiskListView(generic.ObjectListView):
    queryset = models.VMDisk.objects.all()
    table = tables.VMDiskTable

class DiskEditView(generic.ObjectEditView):
    queryset = models.Disk.objects.all()
    form = forms.DiskForm

class DiskSetEditView(generic.ObjectEditView):
    queryset = models.DiskSet.objects.all()
    form = forms.DiskSetForm

class LogicalDriveEditView(generic.ObjectEditView):
    queryset = models.LogicalDrive.objects.all()
    form = forms.LogicalDriveForm

class FilesystemEditView(generic.ObjectEditView):
    queryset = models.Filesystem.objects.all()
    form = forms.FilesystemForm

class ShareEditView(generic.ObjectEditView):
    queryset = models.Share.objects.all()
    form = forms.ShareForm

class SANVolumeEditView(generic.ObjectEditView):
    queryset = models.SANVolume.objects.all()
    form = forms.SANVolumeForm

class ObjectStorageEditView(generic.ObjectEditView):
    queryset = models.ObjectStorage.objects.all()
    form = forms.ObjectStorageForm

class VMDiskEditView(generic.ObjectEditView):
    queryset = models.VMDisk.objects.all()
    form = forms.VMDiskForm
    
    
# Disk Views
class DiskDeleteView(generic.ObjectDeleteView):
    queryset = models.Disk.objects.all()

class DiskView(generic.ObjectView):
    queryset = models.Disk.objects.all()
    
class DiskImportView(generic.BulkImportView):
    queryset = models.Disk.objects.all()
    model_form = forms.DiskImportForm

class DiskBulkEditView(generic.BulkEditView):
    queryset = models.Disk.objects.all()
    table = tables.DiskTable

class DiskBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Disk.objects.all()
    table = tables.DiskTable

class DiskChangeLogView(generic.ObjectChangeLogView):
    queryset = models.Disk.objects.all()

# DiskSet Views
class DiskSetDeleteView(generic.ObjectDeleteView):
    queryset = models.DiskSet.objects.all()

class DiskSetView(generic.ObjectView):
    queryset = models.DiskSet.objects.all()

class DiskSetImportView(generic.BulkImportView):
    model = models.DiskSet
    queryset = models.DiskSet.objects.all()
    model_form = forms.DiskSetForm
    
class DiskSetBulkEditView(generic.BulkEditView):
    queryset = models.DiskSet.objects.all()
    table = tables.DiskSetTable

class DiskSetBulkDeleteView(generic.BulkDeleteView):
    queryset = models.DiskSet.objects.all()
    table = tables.DiskSetTable

class DiskSetChangeLogView(generic.ObjectChangeLogView):
    queryset = models.DiskSet.objects.all()

# LogicalDrive Views
class LogicalDriveDeleteView(generic.ObjectDeleteView):
    queryset = models.LogicalDrive.objects.all()

class LogicalDriveView(generic.ObjectView):
    queryset = models.LogicalDrive.objects.all()

class LogicalDriveImportView(generic.BulkImportView):
    model = models.LogicalDrive
    queryset = models.LogicalDrive.objects.all()
    model_form = forms.LogicalDriveForm
    
class LogicalDriveBulkEditView(generic.BulkEditView):
    queryset = models.LogicalDrive.objects.all()
    table = tables.LogicalDriveTable

class LogicalDriveBulkDeleteView(generic.BulkDeleteView):
    queryset = models.LogicalDrive.objects.all()
    table = tables.LogicalDriveTable

class LogicalDriveChangeLogView(generic.ObjectChangeLogView):
    queryset = models.LogicalDrive.objects.all()

# Filesystem Views
class FilesystemDeleteView(generic.ObjectDeleteView):
    queryset = models.Filesystem.objects.all()

class FilesystemView(generic.ObjectView):
    queryset = models.Filesystem.objects.all()

class FilesystemImportView(generic.BulkImportView):
    model = models.Filesystem
    queryset = models.Filesystem.objects.all()
    model_form = forms.FilesystemForm
    
class FilesystemBulkEditView(generic.BulkEditView):
    queryset = models.Filesystem.objects.all()
    table = tables.FilesystemTable

class FilesystemBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Filesystem.objects.all()
    table = tables.FilesystemTable

class FilesystemChangeLogView(generic.ObjectChangeLogView):
    queryset = models.Filesystem.objects.all()

# Share Views
class ShareDeleteView(generic.ObjectDeleteView):
    queryset = models.Share.objects.all()

class ShareView(generic.ObjectView):
    queryset = models.Share.objects.all()

class ShareImportView(generic.BulkImportView):
    model = models.Share
    queryset = models.Share.objects.all()
    model_form = forms.ShareForm
    
class ShareBulkEditView(generic.BulkEditView):
    queryset = models.Share.objects.all()
    table = tables.ShareTable

class ShareBulkDeleteView(generic.BulkDeleteView):
    queryset = models.Share.objects.all()
    table = tables.ShareTable

class ShareChangeLogView(generic.ObjectChangeLogView):
    queryset = models.Share.objects.all()

# SANVolume Views
class SANVolumeDeleteView(generic.ObjectDeleteView):
    queryset = models.SANVolume.objects.all()

class SANVolumeView(generic.ObjectView):
    queryset = models.SANVolume.objects.all()

class SANVolumeImportView(generic.BulkImportView):
    model = models.SANVolume
    queryset = models.SANVolume.objects.all()
    model_form = forms.SANVolumeForm

class SANVolumeBulkEditView(generic.BulkEditView):
    queryset = models.SANVolume.objects.all()
    table = tables.SANVolumeTable

class SANVolumeBulkDeleteView(generic.BulkDeleteView):
    queryset = models.SANVolume.objects.all()
    table = tables.SANVolumeTable

class SANVolumeChangeLogView(generic.ObjectChangeLogView):
    queryset = models.SANVolume.objects.all()

# ObjectStorage Views
class ObjectStorageDeleteView(generic.ObjectDeleteView):
    queryset = models.ObjectStorage.objects.all()

class ObjectStorageView(generic.ObjectView):
    queryset = models.ObjectStorage.objects.all()

class ObjectStorageImportView(generic.BulkImportView):
    model = models.ObjectStorage
    queryset = models.ObjectStorage.objects.all()
    model_form = forms.ObjectStorageForm
    
class ObjectStorageBulkEditView(generic.BulkEditView):
    queryset = models.ObjectStorage.objects.all()
    table = tables.ObjectStorageTable

class ObjectStorageBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ObjectStorage.objects.all()
    table = tables.ObjectStorageTable

class ObjectStorageChangeLogView(generic.ObjectChangeLogView):
    queryset = models.ObjectStorage.objects.all()

# VMDisk Views
class VMDiskDeleteView(generic.ObjectDeleteView):
    queryset = models.VMDisk.objects.all()

class VMDiskView(generic.ObjectView):
    queryset = models.VMDisk.objects.all()

class VMDiskImportView(generic.BulkImportView):
    model = models.VMDisk
    queryset = models.VMDisk.objects.all()
    model_form = forms.VMDiskForm
    
class VMDiskBulkEditView(generic.BulkEditView):
    queryset = models.VMDisk.objects.all()
    table = tables.VMDiskTable

class VMDiskBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VMDisk.objects.all()
    table = tables.VMDiskTable

class VMDiskChangeLogView(generic.ObjectChangeLogView):
    queryset = models.VMDisk.objects.all()
 
 
@register_model_view(Device, 'disks', path='disks')
class DeviceDisksView(generic.ObjectView):
    """
    Display a tab on the Device detail page listing associated Disks.
    """
    queryset = Device.objects.all()
    template_name = 'netbox_storage_plugin/device_disks_tab.html'

    tab = ViewTab(
        label='Disks',
        badge=lambda obj: models.Disk.objects.filter(
            associated_object_type=ContentType.objects.get_for_model(Device),
            associated_object_id=obj.pk
        ).count() or 0,
    )

    def get_extra_context(self, request, instance):
        if not instance:
            return {'disks_table': None}
        try:
            # Filter Disks associated with this Device via GenericForeignKey
            disks = models.Disk.objects.filter(
                associated_object_type=ContentType.objects.get_for_model(Device),
                associated_object_id=instance.pk
            )
            disks_table = tables.DiskTable(disks)
            disks_table.configure(request)
        except Exception as e:
            disks_table = None
        return {
            'disks_table': disks_table,
        }