from netbox.views import generic
from . import models, forms, tables

class DiskListView(generic.ObjectListView):
    template_name = 'netbox_storage_plugin/storage_list.html'
    queryset = models.Disk.objects.all()
    table = tables.DiskTable

class DiskSetListView(generic.ObjectListView):
    template_name = 'netbox_storage_plugin/storage_list.html'
    queryset = models.DiskSet.objects.all()
    table = tables.DiskSetTable

class LogicalDriveListView(generic.ObjectListView):
    template_name = 'netbox_storage_plugin/storage_list.html'
    queryset = models.LogicalDrive.objects.all()
    table = tables.LogicalDriveTable

class FilesystemListView(generic.ObjectListView):
    template_name = 'netbox_storage_plugin/storage_list.html'
    queryset = models.Filesystem.objects.all()
    table = tables.FilesystemTable

class ShareListView(generic.ObjectListView):
    template_name = 'netbox_storage_plugin/storage_list.html'
    queryset = models.Share.objects.all()
    table = tables.ShareTable

class SANVolumeListView(generic.ObjectListView):
    template_name = 'netbox_storage_plugin/storage_list.html'
    queryset = models.SANVolume.objects.all()
    table = tables.SANVolumeTable

class ObjectStorageListView(generic.ObjectListView):
    template_name = 'netbox_storage_plugin/storage_list.html'
    queryset = models.ObjectStorage.objects.all()
    table = tables.ObjectStorageTable

class VirtualDiskListView(generic.ObjectListView):
    template_name = 'netbox_storage_plugin/storage_list.html'
    queryset = models.VirtualDisk.objects.all()
    table = tables.VirtualDiskTable

class DiskEditView(generic.ObjectEditView):
    template_name = 'netbox_storage_plugin/storage_edit.html'
    queryset = models.Disk.objects.all()
    form = forms.DiskForm

class DiskSetEditView(generic.ObjectEditView):
    template_name = 'netbox_storage_plugin/storage_edit.html'
    queryset = models.DiskSet.objects.all()
    form = forms.DiskSetForm

class LogicalDriveEditView(generic.ObjectEditView):
    template_name = 'netbox_storage_plugin/storage_edit.html'
    queryset = models.LogicalDrive.objects.all()
    form = forms.LogicalDriveForm

class FilesystemEditView(generic.ObjectEditView):
    template_name = 'netbox_storage_plugin/storage_edit.html'
    queryset = models.Filesystem.objects.all()
    form = forms.FilesystemForm

class ShareEditView(generic.ObjectEditView):
    template_name = 'netbox_storage_plugin/storage_edit.html'
    queryset = models.Share.objects.all()
    form = forms.ShareForm

class SANVolumeEditView(generic.ObjectEditView):
    template_name = 'netbox_storage_plugin/storage_edit.html'
    queryset = models.SANVolume.objects.all()
    form = forms.SANVolumeForm

class ObjectStorageEditView(generic.ObjectEditView):
    template_name = 'netbox_storage_plugin/storage_edit.html'
    queryset = models.ObjectStorage.objects.all()
    form = forms.ObjectStorageForm

class VirtualDiskEditView(generic.ObjectEditView):
    template_name = 'netbox_storage_plugin/storage_edit.html'
    queryset = models.VirtualDisk.objects.all()
    form = forms.VirtualDiskForm
    
    
# Disk Views
class DiskDeleteView(generic.ObjectDeleteView):
    queryset = models.Disk.objects.all()

class DiskView(generic.ObjectView):
    queryset = models.Disk.objects.all()
    
class DiskImportView(generic.BulkImportView):
    model = models.Disk

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

class ObjectStorageBulkEditView(generic.BulkEditView):
    queryset = models.ObjectStorage.objects.all()
    table = tables.ObjectStorageTable

class ObjectStorageBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ObjectStorage.objects.all()
    table = tables.ObjectStorageTable

class ObjectStorageChangeLogView(generic.ObjectChangeLogView):
    queryset = models.ObjectStorage.objects.all()

# VirtualDisk Views
class VirtualDiskDeleteView(generic.ObjectDeleteView):
    queryset = models.VirtualDisk.objects.all()

class VirtualDiskView(generic.ObjectView):
    queryset = models.VirtualDisk.objects.all()

class VirtualDiskImportView(generic.BulkImportView):
    model = models.VirtualDisk

class VirtualDiskBulkEditView(generic.BulkEditView):
    queryset = models.VirtualDisk.objects.all()
    table = tables.VirtualDiskTable

class VirtualDiskBulkDeleteView(generic.BulkDeleteView):
    queryset = models.VirtualDisk.objects.all()
    table = tables.VirtualDiskTable

class VirtualDiskChangeLogView(generic.ObjectChangeLogView):
    queryset = models.VirtualDisk.objects.all()
 