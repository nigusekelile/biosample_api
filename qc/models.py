from django.db import models
from samples.models import BioSample

class QCCheck(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    rule = models.CharField(max_length=255)  # E.g., "required: organism"
    
    def __str__(self):
        return self.name


class QCReport(models.Model):
    sample = models.ForeignKey(BioSample, on_delete=models.CASCADE)
    qc_check = models.ForeignKey(QCCheck, on_delete=models.CASCADE)
    passed = models.BooleanField(default=False)
    message = models.TextField()
    checked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sample.accession} - {self.qc_check.name}"
