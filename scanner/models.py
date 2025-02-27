from django.db import models

class ScanResult(models.Model):
    domain = models.CharField(max_length=255)
    ip = models.GenericIPAddressField()
    ports = models.TextField()
    scan_result = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.domain
    

