from netbox.api.viewsets import NetBoxModelViewSet
from ..models import Volume
from .serializers import VolumeSerializer

class VolumeViewSet(NetBoxModelViewSet):
    queryset = Volume.objects.all()
    serializer_class = VolumeSerializer