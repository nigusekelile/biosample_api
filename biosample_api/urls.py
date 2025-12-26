from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from samples.views import BioSampleViewSet, MetadataFieldViewSet, MetadataValueViewSet
from qc.views import QCCheckViewSet, QCReportViewSet
from users.views import CustomAuthToken

router = DefaultRouter()
router.register("biosamples", BioSampleViewSet)
router.register("metadata-fields", MetadataFieldViewSet)
router.register("metadata-values", MetadataValueViewSet)
router.register("qc-checks", QCCheckViewSet)
router.register("qc-reports", QCReportViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/auth/", CustomAuthToken.as_view()),
]
