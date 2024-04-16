from django.contrib import admin
from apps.branch.models.branches import Branch
from apps.branch.models.room import Room


admin.site.register(Branch)
admin.site.register(Room)