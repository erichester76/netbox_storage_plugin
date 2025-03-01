from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from netbox.models import NetBoxModel

class Volume(NetBoxModel):
    """Represents a storage entity in NetBox."""

    # Choices for the type field
    VOLUME_TYPES = (
        ('disk', 'Disk'),
        ('disk_set', 'Disk Set'),
        ('logical_drive', 'Logical Drive'),
        ('filesystem', 'Filesystem'),
        ('share', 'Share'),
        ('san_volume', 'SAN Volume'),
        ('object_storage', 'Object Storage'),
    )

    # Fields
    name = models.CharField(
        max_length=255,
        help_text="A human-readable name for the volume (e.g., 'Disk 1', 'Data Share')"
    )
    type = models.CharField(
        max_length=50,
        choices=VOLUME_TYPES,
        help_text="The type of storage entity"
    )
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        help_text="The parent volume, if this volume is part of a hierarchy (e.g., a filesystem on a logical drive)"
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="The type of object this volume is associated with (e.g., Device, VirtualMachine, VirtualDisk)"
    )
    object_id = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text="The ID of the associated object"
    )
    associated_object = GenericForeignKey(
        'content_type',
        'object_id',
        help_text="The device, virtual machine, virtual disk, or other object this volume is linked to"
    )
    size = models.PositiveBigIntegerField(
        null=True,
        blank=True,
        help_text="The size of the volume in bytes (e.g., 1073741824 for 1 GB)"
    )
    details = models.JSONField(
        null=True,
        blank=True,
        help_text="Type-specific attributes (e.g., {'raid_level': 5} for a disk set, {'protocol': 'nfs'} for a share)"
    )
    description = models.TextField(
        null=True,
        blank=True,
        help_text="Additional notes or context about the volume"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Volume"
        verbose_name_plural = "Volumes"