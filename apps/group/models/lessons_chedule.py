from django.db import models
from apps.core.choicearreyfield import ChoiceArrayField
from apps.group.models.group import Group
from apps.branch.models.room import Room

WEEK_DAYS = [
    ('Dushanba', 'Dushanba'),
    ('Seshanba', 'Seshanba'),
    ('Chorshanba', 'Chorshanba'),
    ('Payshanba', 'Payshanba'),
    ('Juma', 'Juma'),
    ('Shanba', 'Shanba'),
    ('Yakshanba', 'Yakshanba'),
]

class LessonsChedule(models.Model):
    
    start_time = models.TimeField()
    end_time = models.TimeField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    deys = ChoiceArrayField(models.CharField(max_length=32, choices=WEEK_DAYS), null=True, size=64)


    def __str__(self) -> str:
        return self.group_id.name

