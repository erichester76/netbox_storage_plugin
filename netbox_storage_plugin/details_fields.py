from django import forms

"""
details_fields.py

This module defines the fields for each volume type used in the NetBox Storage Plugin.
Each entry in the DETAILS_FIELDS dictionary corresponds to a volume type and contains
a list of field definitions. Each field definition includes the form field name,
the JSON key it maps to, the field class, and keyword arguments for the field.
"""


# relationships.py
RELATIONSHIP_RULES = {
    'disk': {
        'allowed_parents': [],  
        'allowed_associations': ['dcim.Device'],
        'max_depth': 1,  
        'multiple_parents': False,
        'multiple_associations': False,
    },
    'disk_set': {
        'allowed_parents': ['disk'],
        'allowed_associations': ['dcim.Device'],
        'max_depth': 2, 
        'multiple_parents': True,  #
        'multiple_associations': False,
    },
    'logical_drive': {
        'allowed_parents': ['disk_set'],
        'allowed_associations': ['dcim.Device'],
        'max_depth': 3,
        'multiple_parents': False,
        'multiple_associations': False,
    },
    'filesystem': {
        'allowed_parents': ['logical_drive', 'san_volume'],
        'allowed_associations': ['dcim.Device', 'virtualization.VirtualMachine'],
        'max_depth': 4,
        'multiple_parents': False,
        'multiple_associations': True, 
    },
    'share': {
        'allowed_parents': ['filesystem'],
        'allowed_associations': ['dcim.Device'],
        'max_depth': 5,
        'multiple_parents': False,
        'multiple_associations': False,
    },
    'san_volume': {
        'allowed_parents': ['logical_drive'],
        'allowed_associations': ['dcim.Device'],
        'max_depth': 3,
        'multiple_parents': False,
        'multiple_associations': False,
    },
    'object_storage': {
        'allowed_parents': [],
        'allowed_associations': ['dcim.Device', 'virtualization.VirtualMachine'],
        'max_depth': 1,
        'multiple_parents': False,
        'multiple_associations': True,
    },
    'virtual_disk': {
        'allowed_parents': ['filesystem'],
        'allowed_associations': ['virtualization.VirtualDisk'],
        'max_depth': 5,
        'multiple_parents': False,
        'multiple_associations': False,
    },
}

import django.forms as forms

DETAILS_FIELDS = {
    'disk': [
        {
            'form_field': 'disk_interface',
            'json_key': 'interface',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Interface', 'help_text': 'The interface type (e.g., SATA, NVMe)', 'required': True}
        },
        {
            'form_field': 'disk_speed',
            'json_key': 'speed',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Speed', 'help_text': 'The disk speed (e.g., 7200 RPM)', 'required': True}
        },
        {
            'form_field': 'disk_size',
            'json_key': 'size',
            'field_class': forms.IntegerField,
            'kwargs': {'label': 'Size', 'help_text': 'The size in bytes (e.g., 1073741824 for 1 GB)', 'required': True}
        },
    ],
    'disk_set': [
        {
            'form_field': 'disk_set_type',
            'json_key': 'type',
            'field_class': forms.ChoiceField,
            'kwargs': {
                'choices': [('raid', 'RAID'), ('jbod', 'JBOD')],
                'label': 'Type',
                'help_text': 'The type of disk set',
                'required': True
            }
        },
        {
            'form_field': 'disk_set_raid_level',
            'json_key': 'raid_level',
            'field_class': forms.ChoiceField,
            'kwargs': {
                'choices': [(0, 'RAID 0'), (1, 'RAID 1'), (5, 'RAID 5'), (10, 'RAID 10')],
                'label': 'RAID Level',
                'help_text': 'The RAID level',
                'required': True
            }
        },
        {
            'form_field': 'disk_set_disk_count',
            'json_key': 'disk_count',
            'field_class': forms.IntegerField,
            'kwargs': {'label': 'Disk Count', 'help_text': 'Number of disks in the set', 'required': True}
        },
    ],
    'logical_drive': [
        {
            'form_field': 'logical_drive_type',
            'json_key': 'type',
            'field_class': forms.ChoiceField,
            'kwargs': {
                'choices': [('partition', 'Partition'), ('lvm', 'LVM'), ('other', 'Other')],
                'label': 'Type',
                'help_text': 'The type of logical drive',
                'required': True
            }
        },
        {
            'form_field': 'logical_drive_identifier',
            'json_key': 'identifier',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Identifier', 'help_text': 'The identifier (e.g., sda1, vg_data/lv_home)', 'required': True}
        },
        {
            'form_field': 'logical_drive_size',
            'json_key': 'size',
            'field_class': forms.IntegerField,
            'kwargs': {'label': 'Size', 'help_text': 'The size in bytes', 'required': True}
        },
    ],
    'filesystem': [
        {
            'form_field': 'filesystem_type',
            'json_key': 'fs_type',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Filesystem Type', 'help_text': 'The type (e.g., ext4, xfs)', 'required': True}
        },
        {
            'form_field': 'filesystem_mount_point',
            'json_key': 'mount_point',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Mount Point', 'help_text': 'The mount point (e.g., /mnt/data)', 'required': True}
        },
    ],
    'share': [
        {
            'form_field': 'share_protocol',
            'json_key': 'protocol',
            'field_class': forms.ChoiceField,
            'kwargs': {
                'choices': [('nfs', 'NFS'), ('smb', 'SMB'), ('cifs', 'CIFS')],
                'label': 'Protocol',
                'help_text': 'The sharing protocol',
                'required': True
            }
        },
        {
            'form_field': 'share_export_path',
            'json_key': 'export_path',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Export Path', 'help_text': 'The path where the share is exported', 'required': True}
        },
    ],
    'san_volume': [
        {
            'form_field': 'san_protocol',
            'json_key': 'protocol',
            'field_class': forms.ChoiceField,
            'kwargs': {
                'choices': [('iscsi', 'iSCSI'), ('fc', 'Fibre Channel'), ('fcoe', 'FCoE')],
                'label': 'Protocol',
                'help_text': 'The SAN protocol',
                'required': True
            }
        },
        {
            'form_field': 'san_target',
            'json_key': 'target',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Target', 'help_text': 'The target identifier (e.g., IQN)', 'required': True}
        },
        {
            'form_field': 'san_lun_id',
            'json_key': 'lun_id',
            'field_class': forms.IntegerField,
            'kwargs': {'label': 'LUN ID', 'help_text': 'The LUN identifier', 'required': True}
        },
        {
            'form_field': 'san_size',
            'json_key': 'size',
            'field_class': forms.IntegerField,
            'kwargs': {'label': 'Size', 'help_text': 'The size in bytes', 'required': True}
        },
    ],
    'object_storage': [
        {
            'form_field': 'object_storage_provider',
            'json_key': 'provider',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Provider', 'help_text': 'The cloud provider (e.g., AWS)', 'required': True}
        },
        {
            'form_field': 'object_storage_region',
            'json_key': 'region',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Region', 'help_text': 'The storage region (e.g., us-east-1)', 'required': True}
        },
        {
            'form_field': 'object_storage_bucket_name',
            'json_key': 'bucket_name',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Bucket Name', 'help_text': 'The name of the bucket', 'required': True}
        },
    ],
    'virtual_disk': [
        {
            'form_field': 'virtual_disk_format',
            'json_key': 'format',
            'field_class': forms.ChoiceField,
            'kwargs': {
                'choices': [('vmdk', 'VMDK'), ('qcow2', 'QCOW2'), ('vdi', 'VDI')],
                'label': 'Format',
                'help_text': 'The file format of the virtual disk',
                'required': True
            }
        },
        {
            'form_field': 'virtual_disk_provisioning',
            'json_key': 'provisioning',
            'field_class': forms.ChoiceField,
            'kwargs': {
                'choices': [('thin', 'Thin'), ('thick', 'Thick'), ('lazy', 'Lazy Zeroed Thick')],
                'label': 'Provisioning',
                'help_text': 'The provisioning type',
                'required': True
            }
        },
        {
            'form_field': 'virtual_disk_controller',
            'json_key': 'controller',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Controller', 'help_text': 'The controller type (e.g., SCSI)', 'required': True}
        },
        {
            'form_field': 'virtual_disk_path',
            'json_key': 'path',
            'field_class': forms.CharField,
            'kwargs': {'label': 'Path', 'help_text': 'The path to the virtual disk file', 'required': True}
        },
        {
            'form_field': 'virtual_disk_size',
            'json_key': 'size',
            'field_class': forms.IntegerField,
            'kwargs': {'label': 'Size', 'help_text': 'The size in bytes', 'required': True}
        },
    ],
}