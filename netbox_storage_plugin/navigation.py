from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

menu = PluginMenu(
    label='Storage', 
    icon_class='mdi mdi-harddisk', 
    items=(
        PluginMenuItem(
            link='plugins:netbox_storage_plugin:volume_list',  
            link_text='Volumes',  
            buttons=(
                PluginMenuButton(
                    link='plugins:netbox_storage_plugin:volume_add',  
                    title='Add',  
                    icon_class='mdi mdi-plus-thick',  
                    color='green',  
                    permissions=['netbox_storage_plugin.add_volume']  
                ),
                PluginMenuButton(
                    link='plugins:netbox_storage_plugin:volume_import',
                    title='Import',  
                    icon_class='mdi mdi-upload',  
                    color='blue',  
                    permissions=['netbox_storage_plugin.import_volume']  
                ),
            )
        ),
    )
)