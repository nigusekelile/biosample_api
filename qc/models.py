from django.db import models
from samples.models import BioSample

class QCCheck(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class QCReport(models.Model):
    biosample = models.ForeignKey(BioSample, on_delete=models.CASCADE)
    qc_check = models.ForeignKey(QCCheck, on_delete=models.CASCADE)
    passed = models.BooleanField()
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
