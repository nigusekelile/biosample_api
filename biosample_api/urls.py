from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from samples.views import BioSampleViewSet, MetadataFieldViewSet, MetadataValueViewSet
from qc.views import QCCheckViewSet, QCReportViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'samples', BioSampleViewSet)
router.register(r'metadata-fields', MetadataFieldViewSet)
router.register(r'metadata-values', MetadataValueViewSet)
router.register(r'qc-checks', QCCheckViewSet)
router.register(r'qc-reports', QCReportViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/token/', obtain_auth_token),
]
