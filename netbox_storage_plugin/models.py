from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from netbox.models import NetBoxModel
from django.urls import reverse

INTERFACE_CHOICES = [
    ('SATA', 'SATA'),
    ('SAS', 'SAS'),
    ('NVMe', 'NVMe'),
    ('SCSI', 'SCSI'),
    ('IDE', 'IDE'),
    ('USB', 'USB'),
    ('FireWire', 'FireWire'),
    ('Thunderbolt', 'Thunderbolt'),
    ('Other', 'Other'),
]

DISKSET_TYPE_CHOICES = [
    ('RAID', 'RAID'),
    ("vdev", "vdev"),
    ('JBOD', 'JBOD'),
    ('Span', 'Span'),
    ('Stripe', 'Stripe'),
    ('Mirror', 'Mirror'),
    ('Concatenated', 'Concatenated'),
    ('Other', 'Other'),
]

RAID_LEVEL_CHOICES = [
    (0, 'RAID 0'),
    (1, 'RAID 1'),
    (5, 'RAID 5'),
    (6, 'RAID 6'),
    (10, 'RAID 10'),
    (50, 'RAID 50'),
    (60, 'RAID 60'),
    (100, 'raidz1'),
    (101, 'raidz2'),
    (102, 'draid')
]

FS_TYPE_CHOICES = [
    ('vmfs', 'vmfs'),
    ('zfs', 'zfs'),
    ('xfs', 'xfs'),
    ('ext4', 'ext4'),
    ('ext3', 'ext3'),
    ('ntfs', 'NTFS'),
    ('refs', 'ReFS'),
    ('fat32', 'FAT32'),
    ('btrfs', 'btrfs'),
    ('hfs+', 'hfs+'),
    ('apfs', 'apfs'),
    ('ufs', 'ufs'),
    ('other', 'Other'),
]

PROVIDER_CHOICES = [
    ('AWS', 'AWS'),
    ('Azure', 'Azure'),
    ('Google Cloud', 'Google Cloud'),
    ('IBM Cloud', 'IBM Cloud'),
    ('Oracle Cloud', 'Oracle Cloud'),
    ('DigitalOcean', 'DigitalOcean'),
    ('Backblaze', 'Backblaze'),
    ('Wasabi', 'Wasabi'),
    ('Other', 'Other'),
]

FORMAT_CHOICES = [
    ('VMDK', 'VMDK'),
    ('QCOW2', 'QCOW2'),
    ('VHDX', 'VHDX'),
    ('VHD', 'VHD'),
    ('RAW', 'RAW'),
]

PROVISIONING_CHOICES = [
    ('thin', 'Thin'),
    ('thick', 'Thick'),
    ('eagerzeroedthick', 'Eager Zeroed Thick'),
    ('lazyzeroedthick', 'Lazy Zeroed Thick'),
    ('sparse', 'Sparse'),
    ('compressed', 'Compressed'),
    ('deduplicated', 'Deduplicated'),
    ('other', 'Other'),
]

CONTROLLER_CHOICES = [
    ('IDE', 'IDE'),
    ('SAS', 'SAS'),
    ('SATA', 'SATA'),
    ('NVMe', 'NVMe'),
    ('SCSI', 'SCSI'),
    ('VirtIO', 'VirtIO'),
    ('Paravirtual', 'Paravirtual'),
    ('AHCI', 'AHCI'),
    ('Other', 'Other'),
]

DISK_SPEED_CHOICES = [
    ('5400', '5400 RPM'),
    ('7200', '7200 RPM'),
    ('10000', '10k RPM'),
    ('15000', '15k RPM'),
    ('SSD', 'SSD'),
    ('NVMe', 'NVMe'),
]

SHARE_PROTOCOL_CHOICES = [
    ('nfs3', 'NFS3'),
    ('nfs4', 'NFS4'),
    ('smb2', 'SMB2'),
    ('smb3', 'SMB3'),
]

SAN_PROTOCOL_CHOICES = [
    ('iscsi', 'iSCSI'),
    ('fc', 'Fibre Channel'),
    ('fcoe', 'FCoE'),
]

LOGICAL_DRIVE_CHOICES = [
    ('partition', 'Partition'),
    ('lvm', 'LVM'),
    ('zpool', 'Zpool'),
    ('other', 'Other'),
]

# Models
class Disk(NetBoxModel):
    name = models.CharField(max_length=255, help_text="A human-readable name for the disk")
    description = models.TextField(blank=True, help_text="Additional notes or context about the disk")
    size = models.PositiveBigIntegerField(null=True, blank=True, help_text="The size of the disk in bytes")
    interface = models.CharField(max_length=50, choices=INTERFACE_CHOICES, help_text="The interface type (e.g., SATA, NVMe)")
    #phy = models.CharField(max_length=50, help_text="The physical id of the disk")
    #encrypted = models.BooleanField(default=False, help_text="Whether the disk is encrypted")
    #multipath = models.BooleanField(default=False, help_text="Whether the disk is part of a multipath configuration")
    speed = models.CharField(max_length=50, choices=DISK_SPEED_CHOICES, help_text="The disk speed (e.g., 7200 RPM, 10k RPM)")
    part_number = models.CharField(blank=True, max_length=50, help_text="The model number of the disk")
    serial_number = models.CharField(blank=True, max_length=50, help_text="The serial number of the disk")
    firmware_version = models.CharField(blank=True, max_length=50, help_text="The firmware version of the disk")
    wwn = models.CharField(blank=True, max_length=50, help_text="The World Wide Name (WWN) of the disk")

    associated_object_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    associated_object_id = models.PositiveIntegerField(null=True, blank=True)
    associated_object = GenericForeignKey('associated_object_type', 'associated_object_id')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Disk'
        verbose_name_plural = 'Disks'
        
    def get_absolute_url(self):
        return reverse('plugins:netbox_storage_plugin:disk', kwargs={'pk': self.pk})
    
class DiskSet(NetBoxModel):
    name = models.CharField(max_length=255, help_text="A human-readable name for the disk set")
    description = models.TextField(blank=True, help_text="Additional notes or context about the disk set")
    size = models.PositiveBigIntegerField(null=True, blank=True, help_text="The size of the disk set in bytes")

    parent_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, related_name='parent_diskset')
    parent_object_id = models.PositiveIntegerField(null=True, blank=True)
    parent = GenericForeignKey('parent_content_type', 'parent_object_id')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    associated_object = GenericForeignKey('content_type', 'object_id')

    type = models.CharField(max_length=50, choices=DISKSET_TYPE_CHOICES, help_text="The type of disk set (e.g., RAID)")
    raid_level = models.IntegerField(choices=RAID_LEVEL_CHOICES, null=True, blank=True, help_text="The RAID level (e.g., 0, 1, 5)")
    disk_count = models.IntegerField(help_text="Number of disks in the set")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Disk Set'
        verbose_name_plural = 'Disk Sets'
        permissions = [
            ('netbox_storage_plugin.view_diskset', 'Can view disk set'),
            ('netbox_storage_plugin.manage_diskset', 'Can manage disk set'),
        ]
        
    def get_absolute_url(self):
        return reverse('storage:diskset_detail', kwargs={'pk': self.pk})

class LogicalDrive(NetBoxModel):
    name = models.CharField(max_length=255, help_text="A human-readable name for the logical drive")
    description = models.TextField(blank=True, help_text="Additional notes or context about the logical drive")
    size = models.PositiveBigIntegerField(null=True, blank=True, help_text="The size of the logical drive in bytes")

    parent_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, related_name='parent_logicaldrive')
    parent_object_id = models.PositiveIntegerField(null=True, blank=True)
    parent = GenericForeignKey('parent_content_type', 'parent_object_id')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    associated_object = GenericForeignKey('content_type', 'object_id')

    type = models.CharField(max_length=50, choices=LOGICAL_DRIVE_CHOICES, help_text="The type of logical drive")
    identifier = models.CharField(max_length=100, help_text="The identifier (e.g., sda1, vg_data/lv_home)")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('storage:logicaldrive_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = 'Logical Drive'
        verbose_name_plural = 'Logical Drives'
        permissions = [
            ('netbox_storage_plugin.view_logicaldrive', 'Can view logical drive'),
            ('netbox_storage_plugin.manage_logicaldrive', 'Can manage logical drive'),
        ]

class Filesystem(NetBoxModel):
    name = models.CharField(max_length=255, help_text="A human-readable name for the filesystem")
    description = models.TextField(blank=True, help_text="Additional notes or context about the filesystem")
    size = models.PositiveBigIntegerField(null=True, blank=True, help_text="The size of the filesystem in bytes")

    parent_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, related_name='parent_filesystem')
    parent_object_id = models.PositiveIntegerField(null=True, blank=True)
    parent = GenericForeignKey('parent_content_type', 'parent_object_id')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    associated_object = GenericForeignKey('content_type', 'object_id')

    fs_type = models.CharField(max_length=50, choices=FS_TYPE_CHOICES, help_text="The type of filesystem (e.g., ext4, xfs, zfs)")
    mount_point = models.CharField(max_length=255, help_text="The mount point (e.g., /mnt/data)")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage_plugin:filesystem_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = 'Filesystem'
        verbose_name_plural = 'Filesystems'
        permissions = [
            ('netbox_storage_plugin.view_filesystem', 'Can view filesystem'),
            ('netbox_storage_plugin.manage_filesystem', 'Can manage filesystem'),
        ]

class Share(NetBoxModel):
    name = models.CharField(max_length=255, help_text="A human-readable name for the share")
    description = models.TextField(blank=True, help_text="Additional notes or context about the share")
    size = models.PositiveBigIntegerField(null=True, blank=True, help_text="The size of the share in bytes")

    parent_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, related_name='parent_share')
    parent_object_id = models.PositiveIntegerField(null=True, blank=True)
    parent = GenericForeignKey('parent_content_type', 'parent_object_id')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    associated_object = GenericForeignKey('content_type', 'object_id')

    protocol = models.CharField(max_length=50, choices=SHARE_PROTOCOL_CHOICES, help_text="The sharing protocol")
    export_path = models.CharField(max_length=255, help_text="The path where the share is exported (e.g., /mnt/share)")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage_plugin:share_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = 'Share'
        verbose_name_plural = 'Shares'
        permissions = [
            ('netbox_storage_plugin.view_share', 'Can view share'),
            ('netbox_storage_plugin.manage_share', 'Can manage share'),
        ]

class SANVolume(NetBoxModel):
    name = models.CharField(max_length=255, help_text="A human-readable name for the SAN volume")
    description = models.TextField(blank=True, help_text="Additional notes or context about the SAN volume")
    size = models.PositiveBigIntegerField(null=True, blank=True, help_text="The size of the SAN volume in bytes")

    parent_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, related_name='parent_sanvolume')
    parent_object_id = models.PositiveIntegerField(null=True, blank=True)
    parent = GenericForeignKey('parent_content_type', 'parent_object_id')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    associated_object = GenericForeignKey('content_type', 'object_id')

    protocol = models.CharField(max_length=50, choices=SAN_PROTOCOL_CHOICES, help_text="The SAN protocol")
    target = models.CharField(max_length=255, help_text="The target identifier (e.g., IQN for iSCSI)")
    lun_id = models.IntegerField(help_text="The LUN identifier")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage_plugin:sanvolume_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = 'SAN Volume'
        verbose_name_plural = 'SAN Volumes'
        permissions = [
            ('netbox_storage_plugin.view_sanvolume', 'Can view SAN volume'),
            ('netbox_storage_plugin.manage_sanvolume', 'Can manage SAN volume'),
        ]

class ObjectStorage(NetBoxModel):
    name = models.CharField(max_length=255, help_text="A human-readable name for the object storage")
    description = models.TextField(blank=True, help_text="Additional notes or context about the object storage")
    size = models.PositiveBigIntegerField(null=True, blank=True, help_text="The size of the object storage in bytes")

    parent_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, related_name='parent_objectstorage')
    parent_object_id = models.PositiveIntegerField(null=True, blank=True)
    parent = GenericForeignKey('parent_content_type', 'parent_object_id')

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    associated_object = GenericForeignKey('content_type', 'object_id')

    provider = models.CharField(max_length=100, choices=PROVIDER_CHOICES, help_text="The cloud provider (e.g., AWS, Azure, Google Cloud)")
    region = models.CharField(max_length=100, help_text="The storage region (e.g., us-east-1)")
    bucket_name = models.CharField(max_length=255, help_text="The name of the bucket")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage_plugin:objectstorage_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = 'Object Storage'
        verbose_name_plural = 'Object Storage'
        permissions = [
            ('netbox_storage_plugin.view_objectstorage', 'Can view object storage'),
            ('netbox_storage_plugin.manage_objectstorage', 'Can manage object storage'),
        ]

class VMDisk(NetBoxModel):
    name = models.CharField(max_length=255, help_text="A human-readable name for the virtual disk")
    description = models.TextField(blank=True, help_text="Additional notes or context about the virtual disk")
    size = models.PositiveBigIntegerField(null=True, blank=True, help_text="The size of the virtual disk in bytes")

    parent_content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True, related_name='parent_VMDisk')
    parent_object_id = models.PositiveIntegerField(null=True, blank=True)
    parent = GenericForeignKey('parent_content_type', 'parent_object_id')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    associated_object = GenericForeignKey('content_type', 'object_id')
    format = models.CharField(max_length=50, choices=FORMAT_CHOICES, help_text="The file format of the virtual disk (e.g., VMDK, QCOW2)")
    provisioning = models.CharField(max_length=50, choices=PROVISIONING_CHOICES, help_text="The provisioning type (e.g., thin, thick)")
    controller = models.CharField(max_length=50, choices=CONTROLLER_CHOICES, help_text="The type of controller the disk is attached to (e.g., IDE, SCSI)")
    path = models.CharField(max_length=255, help_text="The path to the virtual disk file")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('plugins:netbox_storage_plugin:vmdisk_detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['name']
        verbose_name = 'Virtual Disk'
        verbose_name_plural = 'Virtual Disks'
        permissions = [
            ('netbox_storage_plugin.view_vmdisk', 'Can view virtual disk'),
            ('netbox_storage_plugin.manage_vmdisk', 'Can manage virtual disk'),
        ]