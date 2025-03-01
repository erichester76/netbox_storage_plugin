
DETAILS_FIELDS = {
    'disk': [
        {'name': 'interface', 'label': 'Interface', 'widget': forms.CharField},
        {'name': 'speed', 'label': 'Speed', 'widget': forms.CharField},
    ],
    'disk_set': [
        {'name': 'type', 'label': 'Type', 'widget': forms.CharField},
        {'name': 'raid_level', 'label': 'RAID Level', 'widget': forms.IntegerField},
        {'name': 'disk_count', 'label': 'Disk Count', 'widget': forms.IntegerField},
    ],
    'logical_drive': [
        {'name': 'type', 'label': 'Type', 'widget': forms.ChoiceField, 'choices': [('partition', 'Partition'), ('lvm', 'LVM')]},
        {'name': 'identifier', 'label': 'Identifier', 'widget': forms.CharField},
    ],
    'filesystem': [
        {'name': 'fs_type', 'label': 'Filesystem Type', 'widget': forms.CharField},
        {'name': 'mount_point', 'label': 'Mount Point', 'widget': forms.CharField},
    ],
    'share': [
        {'name': 'protocol', 'label': 'Protocol', 'widget': forms.ChoiceField, 'choices': [('nfs', 'NFS'), ('smb', 'SMB')]},
        {'name': 'export_path', 'label': 'Export Path', 'widget': forms.CharField},
    ],
    'san_volume': [
        {'name': 'protocol', 'label': 'Protocol', 'widget': forms.ChoiceField, 'choices': [('iscsi', 'iSCSI'), ('fc', 'Fibre Channel')]},
        {'name': 'target', 'label': 'Target', 'widget': forms.CharField},
        {'name': 'lun_id', 'label': 'LUN ID', 'widget': forms.IntegerField},
    ],
    'object_storage': [
        {'name': 'provider', 'label': 'Provider', 'widget': forms.CharField},
        {'name': 'region', 'label': 'Region', 'widget': forms.CharField},
        {'name': 'bucket_name', 'label': 'Bucket Name', 'widget': forms.CharField},
    ],
}
