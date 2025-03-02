from netbox.plugins import PluginConfig

class StoragePluginConfig(PluginConfig):
    name = 'netbox_storage_plugin'
    verbose_name = 'Storage Plugin'
    description = 'Manage storage volumes in NetBox'
    version = '0.1.0'
    author = 'Eric Hester'
    author_email = 'hester1@clemson.edu'
    base_url = 'storage'
    min_version = '4.1.0'
    max_version = '4.2.99'

config = StoragePluginConfig