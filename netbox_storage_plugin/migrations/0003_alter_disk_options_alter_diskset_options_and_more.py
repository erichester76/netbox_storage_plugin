# Generated by Django 5.1.4 on 2025-03-02 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_storage_plugin', '0002_disk_diskset_filesystem_logicaldrive_objectstorage_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='disk',
            options={'ordering': ['name'], 'permissions': [('netbox_storage_plugin.view_disk', 'Can view disk'), ('netbox_storage_plugin.manage_disk', 'Can manage disk')]},
        ),
        migrations.AlterModelOptions(
            name='diskset',
            options={'ordering': ['name'], 'permissions': [('netbox_storage_plugin.view_diskset', 'Can view disk set'), ('netbox_storage_plugin.manage_diskset', 'Can manage disk set')]},
        ),
        migrations.AlterModelOptions(
            name='filesystem',
            options={'ordering': ['name'], 'permissions': [('netbox_storage_plugin.view_filesystem', 'Can view filesystem'), ('netbox_storage_plugin.manage_filesystem', 'Can manage filesystem')]},
        ),
        migrations.AlterModelOptions(
            name='logicaldrive',
            options={'ordering': ['name'], 'permissions': [('netbox_storage_plugin.view_logicaldrive', 'Can view logical drive'), ('netbox_storage_plugin.manage_logicaldrive', 'Can manage logical drive')]},
        ),
        migrations.AlterModelOptions(
            name='objectstorage',
            options={'ordering': ['name'], 'permissions': [('netbox_storage_plugin.view_objectstorage', 'Can view object storage'), ('netbox_storage_plugin.manage_objectstorage', 'Can manage object storage')]},
        ),
        migrations.AlterModelOptions(
            name='sanvolume',
            options={'ordering': ['name'], 'permissions': [('netbox_storage_plugin.view_sanvolume', 'Can view SAN volume'), ('netbox_storage_plugin.manage_sanvolume', 'Can manage SAN volume')]},
        ),
        migrations.AlterModelOptions(
            name='share',
            options={'ordering': ['name'], 'permissions': [('netbox_storage_plugin.view_share', 'Can view share'), ('netbox_storage_plugin.manage_share', 'Can manage share')]},
        ),
        migrations.AlterModelOptions(
            name='vmdisk',
            options={'ordering': ['name'], 'permissions': [('netbox_storage_plugin.view_vmdisk', 'Can view virtual disk'), ('netbox_storage_plugin.manage_vmdisk', 'Can manage virtual disk')]},
        ),
        migrations.RemoveField(
            model_name='disk',
            name='parent_content_type',
        ),
        migrations.RemoveField(
            model_name='disk',
            name='parent_object_id',
        ),
        migrations.AddField(
            model_name='disk',
            name='firmware_version',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='disk',
            name='part_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='disk',
            name='serial_number',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='disk',
            name='wwn',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]