from django.db import models
from apps.account.models.user import User
from apps.core.models import TimeModelMixin
from apps.branch.models.branches import Branch


class StaffProfile(TimeModelMixin):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='Userstf', on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='staff_image/')
    salary = models.DecimalField(max_digits=25, default=0, decimal_places=2)
    position =  models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.last_name
