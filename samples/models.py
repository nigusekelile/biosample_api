from django.db import models

class BioSample(models.Model):
    accession = models.CharField(max_length=50, unique=True)
    sample_type = models.CharField(max_length=100)
    organism = models.CharField(max_length=100)
    collected_by = models.CharField(max_length=100, null=True, blank=True)
    collection_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.accession


class MetadataField(models.Model):
    name = models.CharField(max_length=100)
    data_type = models.CharField(
        max_length=20,
        choices=[("string", "string"), ("int", "int"), ("float", "float"), ("date", "date")]
    )

    def __str__(self):
        return self.name


class MetadataValue(models.Model):
    sample = models.ForeignKey(BioSample, on_delete=models.CASCADE, related_name="metadata")
    field = models.ForeignKey(MetadataField, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.sample.accession} - {self.field.name}"
