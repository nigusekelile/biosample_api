from rest_framework import viewsets
from .models import QCCheck, QCReport
from .serializers import QCCheckSerializer, QCReportSerializer

class QCCheckViewSet(viewsets.ModelViewSet):
    queryset = QCCheck.objects.all()
    serializer_class = QCCheckSerializer


class QCReportViewSet(viewsets.ModelViewSet):
    queryset = QCReport.objects.all()
    serializer_class = QCReportSerializer
