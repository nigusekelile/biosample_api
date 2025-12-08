from rest_framework import routers
from .views import QCCheckViewSet, QCReportViewSet

router = routers.DefaultRouter()
router.register(r'checks', QCCheckViewSet)
router.register(r'reports', QCReportViewSet)

urlpatterns = router.urls
