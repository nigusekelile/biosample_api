from rest_framework import serializers
from .models import QCCheck, QCReport

class QCCheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = QCCheck
        fields = "__all__"


class QCReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = QCReport
        fields = "__all__"
