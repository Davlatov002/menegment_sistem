from rest_framework import serializers
from apps.group.models.group import Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = [
            'id',
            'name', 
            'staff',
            'student',
            'scienc',
            'branch',
            'start_at',
            'end_at',
            'status',
        ]