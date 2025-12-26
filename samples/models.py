from django.db import models

class BioSample(models.Model):
    sample_id = models.CharField(max_length=100, unique=True)
    organism = models.CharField(max_length=255)
    collection_date = models.DateField()
    source = models.CharField(max_length=255)

    def __str__(self):
        return self.sample_id


class MetadataField(models.Model):
    name = models.CharField(max_length=100, unique=True)
    required = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class MetadataValue(models.Model):
    biosample = models.ForeignKey(BioSample, on_delete=models.CASCADE)
    field = models.ForeignKey(MetadataField, on_delete=models.CASCADE)
    value = models.TextField()

    class Meta:
        unique_together = ("biosample", "field")
