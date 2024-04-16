from apps.account.models.student_profile import StudentProfile
from django.db import models

class Payment(models.Model):
    
    price_sum = models.DecimalField(default=0, max_digits=20, decimal_places=2)
    student = models.ForeignKey(StudentProfile ,on_delete=models.CASCADE)
    paid_time = models.DateTimeField(auto_now_add=True)
    mothly = models.IntegerField()

    def __str__(self) -> str:
        return self.student_profile.last_name

