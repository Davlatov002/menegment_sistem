from django.contrib import admin
from apps.group.models.group import Group
from apps.group.models.sciences import Scienc
from apps.group.models.lessons_chedule import LessonsChedule

admin.site.register(Group)
admin.site.register(Scienc)
admin.site.register(LessonsChedule)
