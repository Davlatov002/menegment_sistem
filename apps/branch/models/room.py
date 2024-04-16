from .branches import Branch
from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=200)
    number = models.IntegerField()
    max_count = models.IntegerField()
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.number