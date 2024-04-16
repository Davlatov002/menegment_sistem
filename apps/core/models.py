from django.db import models
from django.utils import timezone

class TimeModelMixin(models.Model):
    start_at = models.DateTimeField(default=timezone.now, null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=False)

    class Meta:
        abstract = True


