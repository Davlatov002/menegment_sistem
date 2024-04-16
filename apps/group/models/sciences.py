from django.db import models
from apps.core.models import TimeModelMixin

class Scienc(TimeModelMixin):
    price = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name