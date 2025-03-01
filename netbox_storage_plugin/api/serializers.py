from rest_framework import serializers
from netbox.api.serializers import NetBoxModelSerializer
from ..models import Volume

class VolumeSerializer(NetBoxModelSerializer):
    class Meta:
        model = Volume
        fields = '__all__'