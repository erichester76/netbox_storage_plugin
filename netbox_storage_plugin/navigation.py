from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

# Define menu items for each storage type with Add and Import buttons
items = (
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:disk_list',
        link_text='Disks',
        permissions=['netbox_storage_plugin.view_disk'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:disk_add',
                title='Add',
                icon_class='mdi mdi-plus',
                permissions=['netbox_storage_plugin.add_disk']
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:disk_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=['netbox_storage_plugin.import_disk']
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:diskset_list',
        link_text='Disk Sets',
        permissions=['netbox_storage_plugin.view_diskset'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:diskset_add',
                title='Add',
                icon_class='mdi mdi-plus',
                permissions=['netbox_storage_plugin.add_diskset']
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:diskset_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=['netbox_storage_plugin.import_diskset']
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:logicaldrive_list',
        link_text='Logical Drives',
        permissions=['netbox_storage_plugin.view_logicaldrive'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:logicaldrive_add',
                title='Add',
                icon_class='mdi mdi-plus',
                permissions=['netbox_storage_plugin.add_logicaldrive']
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:logicaldrive_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=['netbox_storage_plugin.import_logicaldrive']
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:filesystem_list',
        link_text='Filesystems',
        permissions=['netbox_storage_plugin.view_filesystem'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:filesystem_add',
                title='Add',
                icon_class='mdi mdi-plus',
                permissions=['netbox_storage_plugin.add_filesystem']
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:filesystem_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=['netbox_storage_plugin.import_filesystem']
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:share_list',
        link_text='Shares',
        permissions=['netbox_storage_plugin.view_share'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:share_add',
                title='Add',
                icon_class='mdi mdi-plus',
                permissions=['netbox_storage_plugin.add_share']
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:share_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=['netbox_storage_plugin.import_share']
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:sanvolume_list',
        link_text='SAN Volumes',
        permissions=['netbox_storage_plugin.view_sanvolume'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:sanvolume_add',
                title='Add',
                icon_class='mdi mdi-plus',
                permissions=['netbox_storage_plugin.add_sanvolume']
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:sanvolume_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=['netbox_storage_plugin.import_sanvolume']
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:objectstorage_list',
        link_text='Object Storage',
        permissions=['netbox_storage_plugin.view_objectstorage'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:objectstorage_add',
                title='Add',
                icon_class='mdi mdi-plus',
                permissions=['netbox_storage_plugin.add_objectstorage']
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:objectstorage_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=['netbox_storage_plugin.import_objectstorage']
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:vmdisk_list',
        link_text='Virtual Disks',
        permissions=['netbox_storage_plugin.view_vmdisk'],
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:vmdisk_add',
                title='Add',
                icon_class='mdi mdi-plus',
                permissions=['netbox_storage_plugin.add_vmdisk']
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:vmdisk_import',
                title='Import',
                icon_class='mdi mdi-upload',
                permissions=['netbox_storage_plugin.import_vmdisk']
            )
        )
    )
)
menu = PluginMenu(
    label='Storage',
    icon_class='mdi mdi-harddisk',
    groups=(('Storage', items),)
)