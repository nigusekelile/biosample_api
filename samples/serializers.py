from rest_framework import serializers
from .models import BioSample, MetadataField, MetadataValue

class MetadataFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetadataField
        fields = "__all__"


class MetadataValueSerializer(serializers.ModelSerializer):
    field = MetadataFieldSerializer()

    class Meta:
        model = MetadataValue
        fields = ["id", "field", "value"]


class BioSampleSerializer(serializers.ModelSerializer):
    metadata = MetadataValueSerializer(many=True, read_only=True)

    class Meta:
        model = BioSample
        fields = "__all__"
