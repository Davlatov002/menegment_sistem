from django.db import models
from apps.core.models import TimeModelMixin

class Branch(TimeModelMixin):
    name = models.CharField(max_length=500)
    address = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name
    