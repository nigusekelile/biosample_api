from rest_framework import viewsets
from .models import BioSample, MetadataField, MetadataValue
from .serializers import (
    BioSampleSerializer,
    MetadataFieldSerializer,
    MetadataValueSerializer
)

class BioSampleViewSet(viewsets.ModelViewSet):
    queryset = BioSample.objects.all()
    serializer_class = BioSampleSerializer


class MetadataFieldViewSet(viewsets.ModelViewSet):
    queryset = MetadataField.objects.all()
    serializer_class = MetadataFieldSerializer


class MetadataValueViewSet(viewsets.ModelViewSet):
    queryset = MetadataValue.objects.all()
    serializer_class = MetadataValueSerializer
