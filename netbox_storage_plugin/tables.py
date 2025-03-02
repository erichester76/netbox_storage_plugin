from netbox.tables import NetBoxTable, columns
import django_tables2 as tables

from .models import Volume

class VolumeTable(NetBoxTable):
    name = tables.Column(linkify=True)
    type = tables.Column()
    size = tables.Column()
    description = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = Volume
        fields = ('name', 'type', 'size', 'description')