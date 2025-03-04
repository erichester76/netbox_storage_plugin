from django.urls import path
from . import views

urlpatterns = [
    # Disk URLs
    path('disks/', views.DiskListView.as_view(), name='disk_list'),
    path('disks/add/', views.DiskEditView.as_view(), name='disk_add'),
    path('disks/<int:pk>/edit/', views.DiskEditView.as_view(), name='disk_edit'),
    path('disks/<int:pk>/delete/', views.DiskDeleteView.as_view(), name='disk_delete'),
    path('disks/<int:pk>/', views.DiskView.as_view(), name='disk-detail'),
    path('disks/import/', views.DiskImportView.as_view(), name='disk_import'),
    path('disks/bulk-edit/', views.DiskBulkEditView.as_view(), name='disk_bulk_edit'),
    path('disks/bulk-delete/', views.DiskBulkDeleteView.as_view(), name='disk_bulk_delete'),
    path('disks/<int:pk>/changelog/', views.DiskChangeLogView.as_view(), name='disk_changelog'),

    # DiskSet URLs
    path('disk-sets/', views.DiskSetListView.as_view(), name='diskset_list'),
    path('disk-sets/add/', views.DiskSetEditView.as_view(), name='diskset_add'),
    path('disk-sets/<int:pk>/edit/', views.DiskSetEditView.as_view(), name='diskset_edit'),
    path('disk-sets/<int:pk>/delete/', views.DiskSetDeleteView.as_view(), name='diskset_delete'),
    path('disk-sets/<int:pk>/', views.DiskSetView.as_view(), name='diskset'),
    path('disk-sets/import/', views.DiskSetImportView.as_view(), name='diskset_import'),
    path('disk-sets/bulk-edit/', views.DiskSetBulkEditView.as_view(), name='diskset_bulk_edit'),
    path('disk-sets/bulk-delete/', views.DiskSetBulkDeleteView.as_view(), name='diskset_bulk_delete'),
    path('disk-sets/<int:pk>/changelog/', views.DiskSetChangeLogView.as_view(), name='diskset_changelog'),

    # LogicalDrive URLs
    path('logical-drives/', views.LogicalDriveListView.as_view(), name='logicaldrive_list'),
    path('logical-drives/add/', views.LogicalDriveEditView.as_view(), name='logicaldrive_add'),
    path('logical-drives/<int:pk>/edit/', views.LogicalDriveEditView.as_view(), name='logicaldrive_edit'),
    path('logical-drives/<int:pk>/delete/', views.LogicalDriveDeleteView.as_view(), name='logicaldrive_delete'),
    path('logical-drives/<int:pk>/', views.LogicalDriveView.as_view(), name='logicaldrive'),
    path('logical-drives/import/', views.LogicalDriveImportView.as_view(), name='logicaldrive_import'),
    path('logical-drives/bulk-edit/', views.LogicalDriveBulkEditView.as_view(), name='logicaldrive_bulk_edit'),
    path('logical-drives/bulk-delete/', views.LogicalDriveBulkDeleteView.as_view(), name='logicaldrive_bulk_delete'),
    path('logical-drives/<int:pk>/changelog/', views.LogicalDriveChangeLogView.as_view(), name='logicaldrive_changelog'),

    # Filesystem URLs
    path('filesystems/', views.FilesystemListView.as_view(), name='filesystem_list'),
    path('filesystems/add/', views.FilesystemEditView.as_view(), name='filesystem_add'),
    path('filesystems/<int:pk>/edit/', views.FilesystemEditView.as_view(), name='filesystem_edit'),
    path('filesystems/<int:pk>/delete/', views.FilesystemDeleteView.as_view(), name='filesystem_delete'),
    path('filesystems/<int:pk>/', views.FilesystemView.as_view(), name='filesystem'),
    path('filesystems/import/', views.FilesystemImportView.as_view(), name='filesystem_import'),
    path('filesystems/bulk-edit/', views.FilesystemBulkEditView.as_view(), name='filesystem_bulk_edit'),
    path('filesystems/bulk-delete/', views.FilesystemBulkDeleteView.as_view(), name='filesystem_bulk_delete'),
    path('filesystems/<int:pk>/changelog/', views.FilesystemChangeLogView.as_view(), name='filesystem_changelog'),

    # Share URLs
    path('shares/', views.ShareListView.as_view(), name='share_list'),
    path('shares/add/', views.ShareEditView.as_view(), name='share_add'),
    path('shares/<int:pk>/edit/', views.ShareEditView.as_view(), name='share_edit'),
    path('shares/<int:pk>/delete/', views.ShareDeleteView.as_view(), name='share_delete'),
    path('shares/<int:pk>/', views.ShareView.as_view(), name='share'),
    path('shares/import/', views.ShareImportView.as_view(), name='share_import'),
    path('shares/bulk-edit/', views.ShareBulkEditView.as_view(), name='share_bulk_edit'),
    path('shares/bulk-delete/', views.ShareBulkDeleteView.as_view(), name='share_bulk_delete'),
    path('shares/<int:pk>/changelog/', views.ShareChangeLogView.as_view(), name='share_changelog'),

    # SANVolume URLs
    path('san-volumes/', views.SANVolumeListView.as_view(), name='sanvolume_list'),
    path('san-volumes/add/', views.SANVolumeEditView.as_view(), name='sanvolume_add'),
    path('san-volumes/<int:pk>/edit/', views.SANVolumeEditView.as_view(), name='sanvolume_edit'),
    path('san-volumes/<int:pk>/delete/', views.SANVolumeDeleteView.as_view(), name='sanvolume_delete'),
    path('san-volumes/<int:pk>/', views.SANVolumeView.as_view(), name='sanvolume'),
    path('san-volumes/import/', views.SANVolumeImportView.as_view(), name='sanvolume_import'),
    path('san-volumes/bulk-edit/', views.SANVolumeBulkEditView.as_view(), name='sanvolume_bulk_edit'),
    path('san-volumes/bulk-delete/', views.SANVolumeBulkDeleteView.as_view(), name='sanvolume_bulk_delete'),
    path('san-volumes/<int:pk>/changelog/', views.SANVolumeChangeLogView.as_view(), name='sanvolume_changelog'),

    # ObjectStorage URLs
    path('object-storages/', views.ObjectStorageListView.as_view(), name='objectstorage_list'),
    path('object-storages/add/', views.ObjectStorageEditView.as_view(), name='objectstorage_add'),
    path('object-storages/<int:pk>/edit/', views.ObjectStorageEditView.as_view(), name='objectstorage_edit'),
    path('object-storages/<int:pk>/delete/', views.ObjectStorageDeleteView.as_view(), name='objectstorage_delete'),
    path('object-storages/<int:pk>/', views.ObjectStorageView.as_view(), name='objectstorage'),
    path('object-storages/import/', views.ObjectStorageImportView.as_view(), name='objectstorage_import'),
    path('object-storages/bulk-edit/', views.ObjectStorageBulkEditView.as_view(), name='objectstorage_bulk_edit'),
    path('object-storages/bulk-delete/', views.ObjectStorageBulkDeleteView.as_view(), name='objectstorage_bulk_delete'),
    path('object-storages/<int:pk>/changelog/', views.ObjectStorageChangeLogView.as_view(), name='objectstorage_changelog'),

    # VirtualDisk URLs
    path('virtual-disks/', views.VMDiskListView.as_view(), name='vmdisk_list'),
    path('virtual-disks/add/', views.VMDiskEditView.as_view(), name='vmdisk_add'),
    path('virtual-disks/<int:pk>/edit/', views.VMDiskEditView.as_view(), name='vmdisk_edit'),
    path('virtual-disks/<int:pk>/delete/', views.VMDiskDeleteView.as_view(), name='vmdisk_delete'),
    path('virtual-disks/<int:pk>/', views.VMDiskView.as_view(), name='vmdisk'),
    path('virtual-disks/import/', views.VMDiskImportView.as_view(), name='vmdisk_import'),
    path('virtual-disks/bulk-edit/', views.VMDiskBulkEditView.as_view(), name='vmdisk_bulk_edit'),
    path('virtual-disks/bulk-delete/', views.VMDiskBulkDeleteView.as_view(), name='vmdisk_bulk_delete'),
    path('virtual-disks/<int:pk>/changelog/', views.VMDiskChangeLogView.as_view(), name='vmdisk_changelog'),
]