from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

# Define menu items for each storage type with Add and Import buttons
items = (
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:disk_list',
        link_text='Disks',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:disk_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:disk_import',
                title='Import',
                icon_class='mdi mdi-upload',
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:diskset_list',
        link_text='Disk Sets',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:diskset_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:diskset_import',
                title='Import',
                icon_class='mdi mdi-upload',
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:logicaldrive_list',
        link_text='Logical Drives',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:logicaldrive_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:logicaldrive_import',
                title='Import',
                icon_class='mdi mdi-upload',
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:filesystem_list',
        link_text='Filesystems',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:filesystem_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:filesystem_import',
                title='Import',
                icon_class='mdi mdi-upload',
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:share_list',
        link_text='Shares',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:share_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:share_import',
                title='Import',
                icon_class='mdi mdi-upload',
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:sanvolume_list',
        link_text='SAN Volumes',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:sanvolume_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:sanvolume_import',
                title='Import',
                icon_class='mdi mdi-upload',
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:objectstorage_list',
        link_text='Object Storages',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:objectstorage_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:objectstorage_import',
                title='Import',
                icon_class='mdi mdi-upload',
            )
        )
    ),
    PluginMenuItem(
        link='plugins:netbox_storage_plugin:virtualdisk_list',
        link_text='Virtual Disks',
        buttons=(
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:virtualdisk_add',
                title='Add',
                icon_class='mdi mdi-plus',
            ),
            PluginMenuButton(
                link='plugins:netbox_storage_plugin:virtualdisk_import',
                title='Import',
                icon_class='mdi mdi-upload',
            )
        )
    )
)
menu = PluginMenu(
    label='Storage',
    icon_class='mdi mdi-harddisk',
    groups=(('Storage', items),)
)