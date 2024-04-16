from django.db import models
from apps.core.models import TimeModelMixin
from apps.account.models.student_profile import StudentProfile
from apps.account.models.staff_profile import StaffProfile
from apps.branch.models.branches import Branch
from .sciences import Scienc

class Group(TimeModelMixin):
    name = models.CharField(max_length=255)
    staff = models.ManyToManyField(StaffProfile)
    student = models.ManyToManyField(StudentProfile)
    scienc = models.ForeignKey(Scienc, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return self.name
    