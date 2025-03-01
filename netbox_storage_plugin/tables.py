from netbox.tables import NetBoxTable, columns
from .models import Volume

class VolumeTable(NetBoxTable):
    name = columns.Column(linkify=True)
    type = columns.Column()
    size = columns.Column()
    description = columns.Column()

    class Meta(NetBoxTable.Meta):
        model = Volume
        fields = ('name', 'type', 'size', 'description')