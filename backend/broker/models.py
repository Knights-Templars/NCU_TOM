from django.db import models

# Create your models here.

class BrokerTarget(models.Model):
    name = models.CharField(max_length=200)
    ra = models.FloatField()
    dec = models.FloatField()
    magnitude = models.FloatField(null=True, blank=True)
    alert_id = models.CharField(max_length=200, unique=True)
    discovered_at = models.FloatField(null=True, blank=True)
    selected = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name} ({self.alert_id})"

        

