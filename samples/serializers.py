from rest_framework import serializers
from .models import BioSample, MetadataField, MetadataValue

class BioSampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BioSample
        fields = "__all__"


class MetadataFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetadataField
        fields = "__all__"


class MetadataValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetadataValue
        fields = "__all__"
