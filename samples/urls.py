from rest_framework import routers
from .views import BioSampleViewSet, MetadataFieldViewSet, MetadataValueViewSet

router = routers.DefaultRouter()
router.register(r'biosamples', BioSampleViewSet)
router.register(r'fields', MetadataFieldViewSet)
router.register(r'metadata', MetadataValueViewSet)

urlpatterns = router.urls
