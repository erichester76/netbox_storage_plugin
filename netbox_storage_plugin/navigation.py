from netbox.plugins import PluginMenu, PluginMenuItem, PluginMenuButton

menu = PluginMenu(
    label='Storage',  # The top-level menu name
    icon_class='mdi mdi-harddisk',  # Icon for the Storage menu (Material Design Icons)
    items=(
        PluginMenuItem(
            link='plugins:netbox_storage_plugin:volume_list',  # URL for the Volumes list view
            link_text='Volumes',  # Display text for the menu item
            buttons=(
                PluginMenuButton(
                    link='plugins:netbox_storage_plugin:volume_add',  # URL for adding a volume
                    title='Add',  # Button label
                    icon_class='mdi mdi-plus-thick',  # Icon for the Add button
                    color='green',  # Button color
                    permissions=['netbox_storage_plugin.add_volume']  # Permission required
                ),
                PluginMenuButton(
                    link='plugins:netbox_storage_plugin:volume_import',  # URL for importing volumes
                    title='Import',  # Button label
                    icon_class='mdi mdi-upload',  # Icon for the Import button
                    color='blue',  # Button color
                    permissions=['netbox_storage_plugin.import_volume']  # Permission required
                ),
            )
        ),
    )
)