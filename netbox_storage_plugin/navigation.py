from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

# Define menu items for each storage type with Add and Import buttons
items = (
    PluginMenuItem(
        link='disk_list',
        link_text='Disks',
        permissions=['netbox_storage_plugin.view_disk'],
        buttons=(
            PluginMenuButton(
                link='disk_add',
                title='Add',
                permissions=['netbox_storage_plugin.add_disk']
            ),
            PluginMenuButton(
                link='disk_import',
                title='Import',
                permissions=['netbox_storage_plugin.import_disk']
            )
        )
    ),
    PluginMenuItem(
        link='disk_set_list',
        link_text='Disk Sets',
        permissions=['netbox_storage_plugin.view_diskset'],
        buttons=(
            PluginMenuButton(
                link='disk_set_add',
                title='Add',
                permissions=['netbox_storage_plugin.add_diskset']
            ),
            PluginMenuButton(
                link='disk_set_import',
                title='Import',
                permissions=['netbox_storage_plugin.import_diskset']
            )
        )
    ),
    PluginMenuItem(
        link='logical_drive_list',
        link_text='Logical Drives',
        permissions=['netbox_storage_plugin.view_logicaldrive'],
        buttons=(
            PluginMenuButton(
                link='logical_drive_add',
                title='Add',
                permissions=['netbox_storage_plugin.add_logicaldrive']
            ),
            PluginMenuButton(
                link='logical_drive_import',
                title='Import',
                permissions=['netbox_storage_plugin.import_logicaldrive']
            )
        )
    ),
    PluginMenuItem(
        link='filesystem_list',
        link_text='Filesystems',
        permissions=['netbox_storage_plugin.view_filesystem'],
        buttons=(
            PluginMenuButton(
                link='filesystem_add',
                title='Add',
                permissions=['netbox_storage_plugin.add_filesystem']
            ),
            PluginMenuButton(
                link='filesystem_import',
                title='Import',
                permissions=['netbox_storage_plugin.import_filesystem']
            )
        )
    ),
    PluginMenuItem(
        link='share_list',
        link_text='Shares',
        permissions=['netbox_storage_plugin.view_share'],
        buttons=(
            PluginMenuButton(
                link='share_add',
                title='Add',
                permissions=['netbox_storage_plugin.add_share']
            ),
            PluginMenuButton(
                link='share_import',
                title='Import',
                permissions=['netbox_storage_plugin.import_share']
            )
        )
    ),
    PluginMenuItem(
        link='san_volume_list',
        link_text='SAN Volumes',
        permissions=['netbox_storage_plugin.view_sanvolume'],
        buttons=(
            PluginMenuButton(
                link='san_volume_add',
                title='Add',
                permissions=['netbox_storage_plugin.add_sanvolume']
            ),
            PluginMenuButton(
                link='san_volume_import',
                title='Import',
                permissions=['netbox_storage_plugin.import_sanvolume']
            )
        )
    ),
    PluginMenuItem(
        link='object_storage_list',
        link_text='Object Storages',
        permissions=['netbox_storage_plugin.view_objectstorage'],
        buttons=(
            PluginMenuButton(
                link='object_storage_add',
                title='Add',
                permissions=['netbox_storage_plugin.add_objectstorage']
            ),
            PluginMenuButton(
                link='object_storage_import',
                title='Import',
                permissions=['netbox_storage_plugin.import_objectstorage']
            )
        )
    ),
    PluginMenuItem(
        link='virtual_disk_list',
        link_text='Virtual Disks',
        permissions=['netbox_storage_plugin.view_virtualdisk'],
        buttons=(
            PluginMenuButton(
                link='virtual_disk_add',
                title='Add',
                permissions=['netbox_storage_plugin.add_virtualdisk']
            ),
            PluginMenuButton(
                link='virtual_disk_import',
                title='Import',
                permissions=['netbox_storage_plugin.import_virtualdisk']
            )
        )
    )
)

# Assign the menu items to the Storage menu
menu = PluginMenu(
    label='Storage',
    icon_class='mdi mdi-harddisk',
    groups=(('Storage', items),)
)