from django.db import models
from apps.account.models.user import User
from apps.core.models import TimeModelMixin

class StudentProfile(TimeModelMixin):
    last_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    phone_number1 = models.CharField(max_length=255)
    phone_number2 = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='students_image/')

    def __str__(self) -> str:
        return self.last_name
